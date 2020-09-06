def personal_inf(name='Кирилл', surname='Добриков', year_birth='1988', city='Москва', email='87909997@gmail.com', tel='+7(916)300-70-35'):

    info_pers = 'Имя: {} Фамилия: {} Год рождения: {} Город проживания: {} Эл.почта: {} Номер телефона: {}'.format(name, surname, year_birth, city, email, tel)
    print(info_pers)
    print(type(info_pers))

personal_inf()
