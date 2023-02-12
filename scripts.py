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
		     'Именно этого я давно ждал от тебя!',
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


def define_schoolkid(name):
    try:
        return Schoolkid.objects.get(full_name__contains=name)
    except Schoolkid.DoesNotExist:
        raise Schoolkid.DoesNotExist("Такого ученика нет")
    except Schoolkid.MultipleObjectsReturned:
        raise Schoolkid.MultipleObjectsReturned\
			('Найдено несколько учеников, уточните ФИО')


def fix_marks(name):
    schoolkid = define_schoolkid(name)
    Mark.objects.filter(schoolkid=schoolkid, points__lt=4).update(points=5)


def remove_chastisements(name):
    schoolkid = define_schoolkid(name)
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(name, subject):
    schoolkid = define_schoolkid(name)
    try:
        lesson = Lesson.objects.filter(
        year_of_study=name.year_of_study,
        group_letter=name.group_letter,
        subject__title=subject
        ).order_by('-date').first()
        if not lesson:
            raise Exception("Урок не найден, похвалу не назначить")
    
    Commendation.objects.create(
    subject=lesson.subject,
    text=random.choice(COMMENDATION_LIST),
    created=lesson.date,
    teacher=lesson.teacher,
    schoolkid=schoolkid
    )
    except AttributeError:
        raise AttributeError("Неправильное название предмета")
