import telebot
from telebot import types
import time

token = '5943542973:AAHv9iVsf_jGwxJprrKxlJkLMINBpBCzwNk'
bot = telebot.TeleBot(token)
dosto = dict([('королевские ворота', "Королевские ворота в Калининграде - одни из семи сохранившихся городских ворот Кёнигсберга. Некогда Королевские ворота были частью фортификационного укрепления в Кенигсберге и служили как по прямому назначению - въезд-выезд из/в город(а) так и в качестве одного из укреплений города-крепости Кёнигсберг. Расположены Королевские ворота на пересечении улицы Фрунзе/Юрия Гагарина и Литовского вала в Калининграде. В настоящее время Королевские ворота - одни из самых интересных в Калининграде. Ворота входят в список достопримечательностей города и являются одним из объектов рекомендованного маршрута «Калининград фортификационный»."), ('дом советов', 'Дом Советов задумывался как место, в котором бы располагалась областная администрация.'), ('куршская коса', 'Большинство туристов приезжает сюда ради отдыха на пляже, а также просмотра уникальных природных образований. Куршская коса, по мнению большинства туристов, считается главной достопримечательностью Калининграда.'), ('танцующий лес', 'Сосновый лес, находящийся на Куршской косе, был высажен 60 лет назад для того, чтобы укрепить пески и защитить их от размывания.'), ('рыбная деревня', 'В Рыбной деревне открываются лучшие виды в Калининграде. Там есть маяк со смотровой площадкой, откуда можно сделать панорамные фото.'), ('фридландские ворота', 'Фридландские ворота середины XIX века стали последними из семи ворот Кенигсберга.'), ('музей изобразительных искусств', 'В городском музее изобразительных искусств представлены работы многих немецких мастеров, датируемых концом XIX — началом XX века.'), ('кафедральный собор', 'Кафедральный собор построили на небольшом островке в центре Кенигсберга. Всемирно известный философ был захоронен у одной из стен собора, а внутри самого здания открыли музей, посвященный Канту.'), ('площадь победы', ' В 1953 здесь установили памятник Иосифу Сталину, но в связи с развенчанием культа личности его заменили на памятник В. И. Ленину.'), ('музей мирового океана', 'В 1994 году Музей Мирового океана стал первым комплексным маринистическим музеем на территории РФ. На экскурсии посетители смогут поближе познакомиться с обитателями морских глубин, в том числе и с теми, которые давно вымерли.'), ('закхаймские ворота', 'Закхаймские ворота в своем современном облике появились в середине XIX века. До этого въезд в Кенигсберг выглядел гораздо проще и являлся частью валового укрепления. Как и остальные из 7 городских ворот, Закхаймские в начале XX века утратили оборонное значение: казематы снесли, валы срыли, а поближе к воротам пристроили жилые дома.'), ('ботанический сад', 'Ботанический сад был основан в начале XX века как сад для исследований Кенигсбергского университета. До начала Второй Мировой войны в его коллекции было больше 4000 видов растений, но все они погибли во время боев за город.'), ('хомлины', 'Легенды гласят, что задолго до людей в окрестностях Кенигсберга обитали хомлины — маленькие сказочные существа. Поговаривают, что они помнят тысячелетнюю историю региона, лучше всех справляются с обработкой янтаря и готовят самый вкусный марципан по оригинальному рецепту...'), ('музей бункер', 'В Бункере находился штаб обороны Кёнигсберга в 1945 году во главе с генералом пехоты Отто Ляшем.'), ('музей янтаря', 'Калининградский областной музей янтаря — единственный в России музей, представляющий многогранную красоту «солнечного камня», был открыт в 1979 году в центре Калининграда, в крепостной башне середины ХIХ века. В его собрании около 15000 украшений и предметов быта из Балтийского самоцвета от эпохи неолита.'), ('кирха святого семейства', 'Кирха построена в 1907 г. по проекту Ф. Хайтманна. Здание выполнено в стиле церкви Тевтонского ордена из красного кирпича. Это готическая ступенчатая постройка с нефом, башней и пристройками.'), ('кенигсбергский замок', 'Уникальная достопримечательность в Калининграде, которую обязательно нужно успеть увидеть. Заложенный в XIII столетии, в разное время Кенигсбергский замок служил цитаделью рыцарей Тевтонского ордена, выполнял функции общественных учреждений Восточной Пруссии.'), ('художественная галерея', 'Это молодая галерея, образованная в 1988 г. Здесь можно увидеть 14 тыс. скульптур, картин, факсимиле, предметов народных промыслов Восточной Пруссии, крупную коллекцию работ художника Э. Белютина, экспозицию работ советской эпохи.'), ('бранденбургские ворота', 'В Калининграде эти ворота единственные, использующиеся по назначению. Они построены в 1657 г., через 100 лет заменены на более прочные, а в середине XIX века украшены цветами и портретами военачальников. Объект находится на ул. Багратиона, 137.'), ('крестовоздвиженский собор', 'До 1933 г. это была лютеранская церковь, после чего ее преобразовали в православный храм по проекту А. Киктона. Здание выделяется необычным стилем, в котором сочетаются элементы неоклассицизма, готики и модерна.'), ('витязь', 'Судно долгие годы занималось экспедициями, побывало во многих государствах. Сейчас оно стало музеем с воссозданными интерьерами кают, кубрика, машинного отека, где можно увидеть уникальные экспозиции на тему судоходства.'), ('башня врангеля', 'Башня из трех этажей — одно из оборонительных укреплений Калининграда, построенное в середине XIX века. Она хорошо сохранилась благодаря толщине наружных стен — 1,35 м. Со всех сторон сооружение окружено рвом с водой.'), ('могила иммануила канта', 'Иммануил Кант — самая известная историческая личность города, легендарный уроженец Кёнигсберга. Философ работал здесь долгие годы, писал научные трактаты, был преподавателем в университете.'), ('памятник барону мюнхгаузену', 'Умеющий рассказывать истории о небывальщине барон Мюнхгаузен пару раз заезжал в город, поэтому калининградцы решили увековечить его в виде силуэта на ядре.'), ('драматический театр', 'Театр образован в 1947 г., а с 1960 г. базируется в здании театра Кенигсберга. Это святилище Мельпомены всегда отличалось дерзкими постановками, но местные режиссёры не забывают и о классике.'), ('биржа', 'Купечество в городе всегда было хорошо развито, благодаря чему появилась биржа, где можно было решать торговые вопросы с городами Ганзейского союза. У Эстакадного моста изначально находилось деревянное задание, которое после пожара было уничтожено.'), ('форт №5', 'Сооружение было построено для охраны дороги на Пилау. Сейчас это музей, где можно увидеть выставку фотографий, а перед зданием выставлена военная техника (пушки, глубинные бомбы, «Катюши»).'), ('бастион грольман', 'Защитное сооружение построено в 1851 г. и названо в честь полководца Грольмана. Это здание из двух этажей с казематами и оросительным валом считается ярким представителем архитектуры 19 в.'), ('юность', 'Находится у Верхнего озера. Здесь есть места для спокойных прогулок, аттракционы, колесо обозрения, лодочная станция и картинг. Здесь часто проводятся городские праздники и фестивали. Находится «Юность» между ул. Тельмана и ул. Азовская.'), ('', '')])
s = []
for i in dosto.keys():
    s.append(i)
s = str(s).replace("]","").replace("[","").replace("'","")
s = s[:-2]

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, 'Привет, я бот который тебе покажет, что можно посмотреть в своём городе. Начнём...')
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Калининград')
    markup.add(itembtn1)
    bot.send_message(message.chat.id, "Выбери город из предложеных:", reply_markup=markup)

@bot.message_handler(content_types = 'text') 
def main(message):
    if message.text=="Калининград":
        bot.send_message(message.chat.id, "Введи название достопримечательность, а я немного про неё расскажу или могу рассказать об основных достопримечательностях города.")
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        itembtn2 = types.KeyboardButton('Рассказать про достопримечательности')
        itembtn3 = types.KeyboardButton('Описать выбранную достопримечательность')
        itembtn4 = types.KeyboardButton('Помощь')
        markup.add(itembtn2, itembtn3, itembtn4)
        bot.send_message(message.chat.id, "Выбери функцию из предложеных:", reply_markup=markup)
    if message.text=="Рассказать про достопримечательности":
        bot.send_message(message.chat.id, 'Я расскажу про основные достопримечательности. После того как прочитаешь про достопримечательность напиши мне что-угодно и я продолжу')
        time.sleep(2)
        sent = bot.send_message(message.chat.id, "Первой будет Рыбная деревня")
        bot.register_next_step_handler(sent, contin) 
    if message.text=="Описать выбранную достопримечательность":
        sent = bot.send_message(message.chat.id, "Напиши название достопримечательности")
        bot.register_next_step_handler(sent, prod)
    if message.text=="Помощь":
        bot.send_message(message.chat.id, f"<b>Вы можете узнать о следующих достопримичательностях:</b> {s}",parse_mode='HTML')
def contin(message):
    sent = bot.send_message(message.chat.id, "В Рыбной деревне открываются лучшие виды в Калининграде. Там есть маяк со смотровой площадкой, откуда можно сделать панорамные фото.")
    bot.register_next_step_handler(sent, contin2)
def contin1(message):
    sent = bot.send_message(message.chat.id, "Напротив Рыбной деревни расположен остров Канта, где находится кафедральный собор Калининграда.")
    bot.register_next_step_handler(sent, contin2)
def contin2(message):
    sent = bot.send_message(message.chat.id, "Второй достопремечательностью про кторосую я расскажу будет Кафедральный собор")
    bot.register_next_step_handler(sent, contin3)
def contin3(message):
    sent = bot.send_message(message.chat.id, "Кафедральный собор - это один из главных символов Калининграда. У стены собора расположена могила великого немецкого мыслителя, профессора Кёнигсбергского университета Иммануила Канта.")
    bot.register_next_step_handler(sent, contin4)
def contin4(message):
    sent = bot.send_message(message.chat.id, "Третей достопремечательностью станет Площадь Победы.")
    bot.register_next_step_handler(sent, contin5)
def contin5(message):
    sent = bot.send_message(message.chat.id, "Площадь Победы - это центральная площадь Калининграда. Сбоку от площади Победы стоит белоснежный Храм Христа Спасителя.")
    bot.register_next_step_handler(sent, contin6)
def contin6(message):
    sent = bot.send_message(message.chat.id, "Четвёртой достопремечательностью про кторосую я расскажу станет Музей мирового океана.")
    bot.register_next_step_handler(sent, contin7)
def contin7(message):
    sent = bot.send_message(message.chat.id, "Музейный комплекс посвящен неистощимым богатствам мирового океана. Комплекс включает главное здание и отдельные суда-музеи.")
    bot.register_next_step_handler(sent, contin8)
def contin8(message):
    sent = bot.send_message(message.chat.id, "Пятой достопримечательностью будет Музей янтаря.")
    bot.register_next_step_handler(sent, contin9)
def contin9(message):
    sent = bot.send_message(message.chat.id, "Экспозиция состоит из нескольких частей и размещается на трёх этажах. В естественно-научном отделе собраны различные образца янтаря — кусочки окаменевшей смолы с насекомыми и растениями возрастом 45-50 млн лет.")
    bot.register_next_step_handler(sent, contin10)
def contin10(message):
    sent = bot.send_message(message.chat.id, "Шестой и последней достопримечательностью о которой я расскажу будет Зоопарк.")
    bot.register_next_step_handler(sent, contin11)
def contin11(message):
    sent = bot.send_message(message.chat.id, "Зоопарк был открыт в 1896 году. Во время Великой Отечественной войны здесь проходили ожесточённые бои, после которых выжили только четверо животных.")
    bot.register_next_step_handler(sent, contin12)
def contin11(message):
    sent = bot.send_message(message.chat.id, "В послевоенное время вольеры снова заполнились зверями, на территории провели перепланировку, устроили детский городок.")
    bot.register_next_step_handler(sent, contin12)
def contin12(message):
    bot.send_message(message.chat.id, "Конец")
    bot.send_message(message.chat.id, "Введи название достопримечательность, а я немного про неё расскажу ил могу рассказать об основных достопримечательностях города.")
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    itembtn2 = types.KeyboardButton('Рассказать про достопримечательности')
    itembtn3 = types.KeyboardButton('Описать выбранную достопримечательность')
    itembtn4 = types.KeyboardButton('Помощь')
    markup.add(itembtn2, itembtn3, itembtn4)
    bot.send_message(message.chat.id, "Выбери функцию из предложеных:", reply_markup=markup)
    if message.text=="Рассказать про достопримечательности":
        bot.send_message(message.chat.id, 'Я расскажу про основные достопримечательности. После того как прочитаешь про достопримечательность напиши мне "продолжай"')
        time.sleep(2)
        sent = bot.send_message(message.chat.id, "Первой будет Рыбная деревня")
        bot.register_next_step_handler(sent, contin)
    if message.text=="Описать выбранную достопримечательность":
        sent = bot.send_message(message.chat.id, "Напиши название достопримечательности")
        bot.register_next_step_handler(sent, prod)
def prod(message):
    message_to_save = message.text
    message_to_save = message_to_save.lower()
    if message_to_save in dosto.keys():
        bot.send_message(message.chat.id, dosto[message_to_save])
    else:
        bot.send_message(message.chat.id, 'Я не знаю такую достопремичательность или название написано с ошибкой')
#run
bot.polling()
