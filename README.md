# Pipe water count
Software to calculate and visualize the amount of water in the pipeline according to the points of the route profile.
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
### Prerequisites
Modules used in the application: PyQt5, pandas, numpy, matplotlib, math. If you don't have some of them, you need to install them sequentially as follows:
```
!pip install PyQt5, pandas, numpy, matplotlib, math.
```
### Running
There are two ways to run the application: through the command line and through an .exe file. If you want to run application by command prompt, you need to run the following command in cmd:
```
python Main_app.py
```
If you want to use application on the local machine without python, you need to convert python files into an .exe file. To do this, you need to run the following command in cmd:
```
pip install pyinstaller
pyinstaller --onefile One_file_app.py
```
## Instruction manual
For running tests for the application, you need to follow the algorithm:
- Run the app.
- Upload necessary data files, by clicking "Загрузить файл" button.
- Choose current file for calculation by clicking it's name in the list of files.
- Set the necessary baseline data.
- Click by button "Построить график".
- Click by button "Сохранить результат в excel формате" to download the result data file.
- Repeat the algorithm to calculate another pipe profile.

Visualization of the application work:
![Screenshot from 2022-08-21 00-50-28](https://user-images.githubusercontent.com/109418051/185767245-bafc88ec-d5d8-4c77-b50b-efd7640dd21e.png)
Visualization of the result data file:
![Screenshot from 2022-08-21 01-02-43](https://user-images.githubusercontent.com/109418051/185767516-3b6f8bd0-ab91-4975-a9e6-47e2811f9976.png)
## Authors
- **Razin Aleksandr** - *Initial work* - [RazinAleksandr](https://github.com/RazinAleksandr)
