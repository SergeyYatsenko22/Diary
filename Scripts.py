from datacenter.models import (Chastisement, Commendation, Lesson,
							   Mark, Schoolkid, Subject)


def fix_marks(schoolkid):
	child_name = Schoolkid.objects.get(full_name=schoolkid).full_name
	Mark.objects.filter(schoolkid__full_name=child_name, points__lt=4).update(points=5)


def remove_chastisements(schoolkid):
	child_name = Schoolkid.objects.get(full_name=schoolkid).full_name
	Chastisement.objects.filter(schoolkid__full_name=child_name).delete()


def create_commendation(schoolkid, to_change):
	import random
	commendation_input = """
	1. Молодец!
	2. Отлично!
	3. Хорошо!
	4. Гораздо лучше, чем я ожидал!
	5. Ты меня приятно удивил!
	6. Великолепно!
	7. Прекрасно!
	8. Ты меня очень обрадовал!
	9. Именно этого я давно ждал от тебя! 
	10. Сказано здорово – просто и ясно!
	11. Ты, как всегда, точен!
	12. Очень хороший ответ!
	13. Талантливо!
	14. Ты сегодня прыгнул выше головы!
	15. Я поражен!
	16. Уже существенно лучше!
	17. Потрясающе!
	18. Замечательно!
	19. Прекрасное начало!
	20. Так держать!
	21. Ты на верном пути!
	22. Здорово!
	23. Это как раз то, что нужно!
	24. Я тобой горжусь!
	25. С каждым разом у тебя получается всё лучше!
	26. Мы с тобой не зря поработали!
	27. Я вижу, как ты стараешься!
	28. Ты растешь над собой!
	29. Ты многое сделал, я это вижу!
	30. Теперь у тебя точно все получится!
	"""
	
	commendation_list = (''.join([word for word in commendation_input
								  if not word.isdigit()])).replace(". ", "").split("\n")
	
	try:
		сhild_name_full = Schoolkid.objects.get(full_name__contains=schoolkid)
		child_subject = Lesson.objects.filter(
			year_of_study=сhild_name_full.year_of_study,
			group_letter=сhild_name_full.group_letter,
			subject__title=to_change
		)
		child_subject_ordered_first = child_subject.order_by('-date').first()
		Commendation.objects.create(
			subject=child_subject_ordered_first.subject,
			text=random.choice(commendation_list),
			created=child_subject_ordered_first.date,
			teacher=child_subject_ordered_first.teacher,
			schoolkid=сhild_name_full
		)
	except AttributeError:
		print("Неправильное название предмета")
