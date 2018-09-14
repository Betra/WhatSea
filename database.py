'''
This is module database
'''

newType = {'govBorders':True,'fauna':True, 'ports':True, 'islands':True, 'gulfs':True, 'rivers':True}



def ComplimentDb(db,name, waterBorders, govBorders, depth, size, color, fauna, temperature, saltiness, position,
 attraction, warFactor, extraction, routes, facts, discoverer, ports, islands, litos, volcanos, gulfs, rivers, ocean):
	'''
	Adds all required data to the end of the database
	'''
	db.append({
		'name':name,
		'waterBorders': waterBorders,
		'govBorders': govBorders,
		'depth': depth,
		'size': size,
		'color': color,
		'fauna': fauna,
		'temperature': temperature,
		'saltiness': saltiness,
		'position': position,
		'attraction': attraction,
		'warFactor': warFactor,
		'extraction': extraction,
		'routes':routes,
		'facts': facts,
		'discoverer': discoverer,
		'ports': ports,
		'islands': islands,
		'litos': litos,
		'volcanos': volcanos,
		'gulfs': gulfs,
		'rivers': rivers,
		'ocean': ocean,
	})

def initStandartSetDb(db = []):
	'''
	Compiles the initial database which is to be trimmed later via subtractive filters
	At some point, somebody, who was filling in this information, probably felt very bad about his life
	At some point, (s)he probably wanted a nice wiki JSON API 
	'''
	ComplimentDb(db,'Японское',
	 	['Желтое','Восточно-китайское','Охотское'],
	  	['Япония', 'КНДР', 'Корея', 'Россия'],
	  	1536,
	  	1062000,
	  	'светлая',
	  	['Осьминог', 'Кальмар', 'Морская Звезда', 'Морской Еж', 'Креветка', 'Краб'],
	  	23,
	  	34,
	  	'восток',
	  	False,
	  	True,
	  	False,
	  	False,
	  	['Россия и Япония'],
	  	'',
	  	['Владивосток','Ниигата','Пусан'],
	  	[],
	  	'Китайская',
	  	True,
	  	['Петра Великого','Восточно-Корейский'],
	  	[],
	  	'Тихий'
	  	)
	ComplimentDb(db,'Азовское',
	 	['Черное'],
	  	['Россия','Украина'],
	  	8,
	  	3900,
	  	'светлая',
	  	['Планктон', 'Сельдь', 'Лещ', 'Морская Свинья'],
	  	22,
	  	10,
	  	'север',
	  	True,
	  	True,
	  	True,
	  	True,
	  	['Россия и Турция'],
		'',
		['Азов','Керчь','Таганрог','Ейск'],
		[],
		'Евразийская',
		False,
		['Таганрогский','Таманский','Арабатский'],
		['Дон'],
		'Атлантический'
	  	)
	ComplimentDb(db,'Балтийское',
	 	['Северное'],
	 	['Россия', 'Финляндия', 'Эстония', 'Латвия', 'Литва', 'Польша', 'Дания', 'Швеция', 'Германия'],
	 	50,
	  	415000,
	  	'темная',
	  	['Шпрот', 'Щука', 'Окунь', 'Килька', 'Треска', 'Угорь', 'Тюлень', 'Сельдевая Акула'],
	  	14,
	  	8,
	  	'север',
	  	True,
	  	True,
	  	True,
	  	True,
	  	['Россия и Германия','Россия и Швеция'],
		'',
		['Санкт-Петербург','Таллин','Рига','Гданьск','Копенгаген','Хельсинки'],
		['Готланд','Кярдла','Курессааре','Хайлуото','Эланд'],
		'Евразийская',
		False,
		['Ботанический','Рижский','Финский'],
		['Нева','Зап. Двина','Висла','Одер'],
		'Атлантический'
	 	)
	ComplimentDb(db,'Красное',
	 	['Средиземное','Аравийское'],
	 	['Египет', 'Судан', 'Эритрея', 'Сомали', 'Саудовская Аравия', 'Израиль', 'Йемен'],
	 	437,
	  	450000,
	  	'светлая',
	  	['Кораллы','Дельфин', 'Косатка', 'Морской Огурец', 'Рыба-ангел', 'Рыба-бабочка', 'Рыба-клоун', 'Султанка'],
	  	27,
	  	41,
	  	'юг',
	  	True,
	  	False,
	  	True,
	  	True,
	  	[],
		'',
		['Суэц','Акаба','Хургада','Джидда','Порт-Судан'],
		[],
		'Аравийская',
		False,
		['Суэцкий','Аденский'],
		[],
		'Индийский'
	 	)
	ComplimentDb(db,'Аравийское',
	 	['Красное'],
	  	['Индия', 'Саудовская Аравия', 'Онам', 'Йемен', 'Пакистан', 'Иран'],
	  	3000,
	  	3862000,
	  	'темная',
	  	['Кораллы','Акула'],
	  	20,
	  	36,
	  	'юг',
	  	True,
	  	False,
	  	True,
	  	True,
	  	[],
		'',
		['Мумбаи','Панаджи','Маскат'],
		[],
		'Аравийская',
		False,
		['Оманский','Аденский'],
		[],
		'Индийский'
	  	)
	ComplimentDb(db,'Белое',
	 	['Баренцево','Печорское'],
	  	['Россия'],
	  	47,
	  	90000,
	  	'темная',
	  	['Тюлень', 'Дельфин', 'Треска', 'Сайга', 'Сельдь', 'Камбала'],
	  	15,
	    30,
	  	'север',
	  	False,
	  	False,
	  	True,
	  	True,
	  	[],
		'',
		['Архангельск'],
		['Большой Соловецкий','Моржовец'],
		'Евразийская',
		False,
		['Кандалакшский'],
		['Мезень'],
		'Северный Ледовитый'
	  	)
	ComplimentDb(db,'Баренцево',
	 	['Белое','Гренландское','Норвежское','Печорское','Карское'],
	  	['Россия'],
	  	222,
	  	1424000,
	  	'темная',
	  	['Треска', 'Сельдь', 'Пикша', 'Окунь', 'Камбала', 'Палтус', 'Белый медведь', 'Белуха', 'Тюлень', 'Краб'],
	  	6,
	  	33,
	  	'север',
	  	False,
	  	True,
	  	True,
	  	True,
	  	[],
		'',
		[],
		['Новая Земля','Спитсберг','Земля Франца-Иосифа'],
		'Евразийская',
		False,
		[],
		[],
		'Северный Ледовитый'
	  	)
	ComplimentDb(db,'Лазарево',
	 	['Уэделла','Рисер-Ларсена'],
	  	[],
	  	3000,
	  	335000,
	  	'темная',
	  	['Тюлень', 'Пингвин', 'Косатка', 'Кит'],
	  	-1,
	  	33,
	  	'север',
	  	False,
		False,
	  	False,
	  	False,
		[],
		'',
		[],
		[],
		'Антарктическая',
		False,
		[],
		[],
		'Южный'
	  	)
	ComplimentDb(db,'Росса',
	 	['Сомова','Амунсдена'],
	  	[],
	  	677,
	  	43900,
	  	'темная',
	  	['Антарктический глупыш', 'Тюлень-крабоед', 'Южный морской полосатик', 'Пингвин', 'Кальмар', 'Морской Леопард'],
	  	-1,
	  	34,
	  	'юг',
	  	False,
		False,
		False,
		False,
	  	[],
		'',
		[],
		[],
		'Антарктическая',
		False,
		[],
		[],
		'Южный'
	  	)
	ComplimentDb(db,'Черное',
	 	['Азовское','Мраморное'],
	  	['Россия', 'Турция', 'Болгария', 'Грузия', 'Абхазия', 'Украина', 'Румыния'],
	  	1240,
	  	422000,
	  	'светлая',
	  	['Мидия', 'Устрица', 'Гребешок', 'Бычок', 'Морской Дракончик'],
	  	20,
	  	15,
	  	'север',
	  	True,
	  	False,
	  	True,
	  	True,
	  	['Россия и Турция','Россия и Германия','Россия, Великобритания и Франция'],
		'',
		['Новоросийск','Севастополь','Одесса','Констанца','Бургас','Самсун','Сухум'],
		[],
		'Евразийская',
		False,
		['Каркинитский'],
		['Дунай','Днепр','Днестр'],
		'Атлантический'
	  	)
	ComplimentDb(db,'Охотское',
	 	['Японское'],
	  	['Россия', 'Япония'],
		821,
		1603000,
	  	'светлая',
	  	['Лосось', 'Сельдь', 'Мойва', 'Камчатский Краб'],
	  	4,
	  	33,
	  	'восток',
	  	False,
	  	False,
	  	True,
	  	True,
	  	[],
		'',
		['Магадан'],
		['Курильские'],
		'Китайская',
		True,
		['Терпения','Шелихова','Анива Академии'],
		['Амур'],
		'Тихий'
	  	)
	ComplimentDb(db,'Желтое',
	 	['Восточно-китайское'],
	  	['КНДР', 'Корея', 'Китай'],
	  	40,
	  	416000,
	  	'темная',
	  	[],
	  	26,
	  	33,
	  	'восток',
	  	False,
	  	False,
	  	True,
	  	False,
	  	[],
		'',
		['Тяньцзинь','Яньтай','Циндао','Нампхо','Инчхон'],
		[],
		'Китайская',
		False,
		['Ляодунский','Бохайвань','Западно-корейский'],
		['Хуанхэ','Хайхэ'],
		'Тихий'
	  	)
	ComplimentDb(db,'Мраморное',
	 	['Черное','Эгейское'],
	  	['Турция'],
	  	500,
	  	11472000,
	  	'светлая',
	  	['Акула'],
	  	29,
	  	25,
	  	'юг',
	  	True,
	  	False,
	  	False,
	  	True,
		[],
		'',
		['Стамбул'],
		['Эрдек','Мармара'],
		'Евразийская',
		False,
		['Гемликский','Бандырма','Эрдек','Измитский'],
		[],
		'Атлантический'
	  	)
	ComplimentDb(db,'Чукотское',
	 	['Восточно-сибирское','Бофорта'],
	  	['Россия', 'США'],
	  	71,
	  	595000,
	  	'темная',
	  	['Белый медведь', 'Морж', 'Кит', 'Тюлень'],
	  	-2,
	  	32,
	  	'север',
	  	False,
	  	False,
	  	True,
	  	True,
	  	[],
		'',
		[],
		['Врангеля'],
		'Северо-Американская',
		False,
		[],
		[],
		'Северный Ледовитый'
	  	)
	ComplimentDb(db,'Норвежское',
	 	['Северное','Гренландское','Баренцево'],
	  	['Норвегия', 'Исландия'],
	  	1700,
	  	1400000,
	  	'темная',
	  	['Треска', 'Сельдь'],
	  	10,
	  	35,
	  	'север',
	  	False,
	  	True,
	  	True,
	  	True,
	  	['Англия и Германия'],
		'',
		['Тронхейм','Тромсё','Нарвик'],
		['Исландия'],
		'Евразийская',
		False,
		[],
		[],
		'Северный Ледовитый'
	  	)
	ComplimentDb(db,'Дюрвиля',
	 	['Сомова','Дейвиса'],
	  	[],
	  	500,
	  	1000000,
	  	'темная',
	  	['Пингвин', 'Косатка', 'Молюск'],
	  	0,
	  	34,
	  	'юг',
	  	False,
	  	False,
	  	False,
	  	False,
	  	[],
		'',
		[],
		[],
		'Антарктическая',
		False,
		[],
		[],
		'Южный'
	  	)
	ComplimentDb(db,'Карское',
	 	['Баренцево','Печорское','Лаптевых'],
	  	['Россия'],
	  	75,
	  	900000,
	  	'темная',
	  	['Окунь', 'Корюшка', 'Морской Заяц', 'Белуха'],
	  	6,
	  	34,
	  	'восток',
	  	False,
	  	True,
	  	True,
	  	True,
	  	[],
		'',
		[],
		['Северная Земля','Новая Земля'],
		'Евразийская',
		False,
		[],
		['Енисей','Обь','Таз'],
		'Северный Ледовитый'
	  	)
	ComplimentDb(db,'Эгейское',
	 	['Мраморное','Средиземное'],
	  	['Швеция', 'Турция'],
	  	150,
	  	179000,
	  	'светлая',
	  	['Осьминог'],
	  	24,
	  	39,
	  	'юг',
	  	True,
	  	False,
	  	False,
	  	True,
		['Англия и Германия','Турция и Греция','Турция и Англия'],
		'',
		['Пирей','Салоники','Измир'],
		['Крит','Родос','Лесбос','Хиос'],
		'Евразийская',
		False,
		['Измирский','Сароникос','Саросский','Термаикос'],
		[],
		'Атлантический'
	  	)
	ComplimentDb(db,'Карибское',
	 	['Саргассово'],
	  	['США', 'Гватемала', 'Гондурас', 'Куба', 'Никарагуа', 'Коста-Рика', 'Венесуэла'],
	  	2500,
	  	2753000,
	  	'светлая',
	  	['Акула', 'Летучая рыба', 'Кашалот', 'Горбатый Кит', 'Дельфин'],
	  	25,
	  	36,
	  	'запад',
	  	True,
	  	False,
	  	True,
	  	True,
		[],
		'',
		['Маракабо','Ла-Гуайра','Картахена','Лимон','Санта-Доминго','Колон','Сантьяго-де-Куба'],
		['Куба','Гаити','Ямайка'],
		'Карибская',
		False,
		['Москитос','Венесуэльский'],
		['Магдалена'],
		'Атлантический'
	  	)
	ComplimentDb(db,'Северное',
	 	['Норвежское','Балтийское'],
	  	['Великобритания', 'Норвегия', 'Дания', 'Швеция', 'Голландия', 'Бельгия', 'Германия'],
	  	95,
	  	750000,
	  	'темная',
	  	['Треска', 'Сельдь', 'Палтус', 'Креветка'],
	  	15,
	  	33,
	  	'запад',
	  	False,
	  	False,
	  	True,
	  	True,
		[],
		'',
		['Роттердам','Амстердам','Антверпен','Лондон','Гамбург','Осло','Берген'],
		['Британские'],
		'Евразийская',
		False,
		[],
		['Эльба','Везер','Рейн','Темза'],
		'Атлантический'
	  	)
	return db

database = initStandartSetDb()

seaNames = []
for sea in database:
	seaNames.append(sea['name'])
seaNames = ", ".join(seaNames)

length = len(seaNames)

if __name__ == '__main__':
	exit()