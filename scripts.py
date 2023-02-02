from datacenter.models import (Chastisement, Commendation, 
			       Lesson, Mark, Schoolkid)
import random
COMMENDATION_LIST = ['Молодец!',
		     'Отлично!',
		     'Хорошо!',
		     'Гораздо лучше, чем я ожидал!',
		     'Ты меня приятно удивил!',
		     'Великолепно!',
		     'Прекрасно!',
		     'Ты меня очень обрадовал!',
		     'Именно этого я давно ждал от тебя! ',
		     'Сказано здорово – просто и ясно!',
		     'Ты, как всегда, точен!',
		     'Очень хороший ответ!',
		     'Талантливо!',
		     'Ты сегодня прыгнул выше головы!',
		     'Я поражен!',
		     'Уже существенно лучше!',
		     'Потрясающе!',
		     'Замечательно!',
		     'Прекрасное начало!',
		     'Так держать!',
		     'Ты на верном пути!',
		     'Здорово!',
		     'Это как раз то, что нужно!',
		     'Я тобой горжусь!',
		     'С каждым разом у тебя получается всё лучше!',
		     'Мы с тобой не зря поработали!',
		     'Я вижу, как ты стараешься!',
		     'Ты растешь над собой!',
		     'Ты многое сделал, я это вижу!',
		     'Теперь у тебя точно все получится!']


def define_schoolkid(schoolkid):
    try:
        return Schoolkid.objects.get(full_name__contains=schoolkid)
    except Schoolkid.DoesNotExist:
        raise Schoolkid.DoesNotExist("Такого ученика нет")


def fix_marks(schoolkid):
    try:
        Mark.objects.filter(schoolkid__full_name=define_schoolkid(schoolkid).
			    full_name, points__lt=4).update(points=5)
    except AttributeError:
        pass
    except Schoolkid.MultipleObjectsReturned:
        raise Schoolkid.MultipleObjectsReturned(
		'Найдено несколько учеников, уточните ФИО')


def remove_chastisements(schoolkid):
    try:
        Chastisement.objects.filter(schoolkid__full_name=define_schoolkid(schoolkid).
				    full_name).delete()
    except AttributeError:
        pass
    except Schoolkid.MultipleObjectsReturned:
        raise Schoolkid.MultipleObjectsReturned(
		'Найдено несколько учеников, уточните ФИО')


def create_commendation(schoolkid, subject):
    name = define_schoolkid(schoolkid)
    try:
        lesson = Lesson.objects.filter(
		year_of_study=name.year_of_study,
		group_letter=name.group_letter,
		subject__title=subject
		).order_by('-date').first()
		Commendation.objects.create(
		subject=lesson.subject,
		text=random.choice(COMMENDATION_LIST),
		created=lesson.date,
		teacher=lesson.teacher,
		schoolkid=Schoolkid.objects.get(full_name__contains=schoolkid)
		)
	if not lesson:
            print("Урок не найден, похвалу не назначить")

    except AttributeError:
        pass
    except Schoolkid.MultipleObjectsReturned:
        raise Schoolkid.MultipleObjectsReturned(
		'Найдено несколько учеников, уточните ФИО')