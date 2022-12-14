# Pipe water count
Software to calculate and visualize the amount of water in the pipeline according to the points of the route profile.
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
### Prerequisites
Modules used in the application: PyQt5, pandas, numpy, matplotlib, math. If you don't have some of them, you need to install them sequentially as follows:
```
!pip install PyQt5, pandas, numpy, matplotlib, math
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
- Upload necessary data files, by clicking "Upload file" button.
- Choose current file for calculation by clicking it's name in the list of files.
- Set the necessary baseline data.
- Click by button "Draw a graph".
- Click by button "Save the result in excel format" to download the result data file.
- Repeat the algorithm to calculate another pipe profile.

Visualization of the application work:
![Screenshot from 2022-08-21 01-24-54](https://user-images.githubusercontent.com/109418051/185768184-bde43583-fcb6-4ad7-92de-e8fd882b2b46.png)
Visualization of the result data file:
![Screenshot from 2022-08-21 01-02-43](https://user-images.githubusercontent.com/109418051/185768190-ef21b611-e979-46b7-86c5-9ec6450937b3.png)
## Authors
- **Razin Aleksandr** - *Initial work* - [RazinAleksandr](https://github.com/RazinAleksandr)
