# FlaskWebS


This is a simple web application created as part of the Modulus 164 project. 

The goal of this project is to show our skills and understanding of web development.

**All database elements (MCD, MLD and dictionary) are in `.github/database`**


[![Version](https://img.shields.io/github/v/release/InstaZDLL/Besson_Ethan_info1a_164_2023?style=for-the-badge)](https://github.com/InstaZDLL/Besson_Ethan_info1a_164_2023/releases)
[![AFLv3 License](https://img.shields.io/github/license/InstaZDLL/Besson_Ethan_info1a_164_2023?logo=e&style=for-the-badge)](https://opensource.org/license/afl-3-0-php)
[![Last commit](https://img.shields.io/github/last-commit/InstaZDLL/Besson_Ethan_info1a_164_2023?style=for-the-badge)](https://github.com/InstaZDLL/Besson_Ethan_info1a_164_2023/commits/main)


[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)


## Software to download before installing

### Required :

###### Windows :
- [Laragon Full](https://laragon.org/download/#Edition) - v6.0.0 or newer.
- [Gitbash](https://git-scm.com/download/win) - v2.41.0 or newer.
- [Python](https://www.python.org/downloads/) - v3.11.3 or newer.

### Optional :

- Pycharm - v2023.1 only if you want to use the other installation.


## Installing the Flask application

### Windows (Gitbash)

Clone the project by opening gitbash or the terminal.

```git
git clone https://github.com/InstaZDLL/Besson_Ethan_info1a_164_2023.git
```

Go to the project directory.

```shell
cd Besson_Ethan_info1a_164_2023
```

[Optional] If you hava Laragon you don't have to edit something if your credentials are root with no password.
Modify the [environment variables](https://github.com/InstaZDLL/Besson_Ethan_info1a_164_2023#environment-variables) in the `.env` file. You can edit the file with Notepad or another text editing tool.

```shell
notepad .env
```

[Optional] If you don't want to change the dump and keep the original database you can skip this step, Change, **if needed**, the `besson_ethan_info_1a.sql` file in the `database` directory. You can edit the file with Notepad or another text editing tool.

```shell
cd FlaskWebS/database
```
```shell
notepad besson_ethan_info_1a.sql
```

Return to the root folder of the project and start the server. You can launch the `start.bat` file with a **double click** or in the terminal with `.\start.bat`.

```shell
.\start.bat
```

#### Installation tutorial for Windows :

Standard installation (Gitbash):

![Standard install](https://raw.githubusercontent.com/InstaZDLL/Besson_Ethan_info1a_164_2023/main/.github/Windows_standard_install_tutorial.gif)

Other installation (PyCharm):

![Idea install](https://raw.githubusercontent.com/InstaZDLL/Besson_Ethan_info1a_164_2023/main/.github/Windows_idea_install_tutorial.gif)

### Linux

Install the following dependency (You must also have installed python3)

```shell
sudo apt install python3-pip
```

Clone the project.

```git
git clone https://github.com/InstaZDLL/Besson_Ethan_info1a_164_2023.git
```

Go to the project directory.

```shell
cd Besson_Ethan_info1a_164_2023
```

Modify the [environment variables](https://github.com/InstaZDLL/Besson_Ethan_info1a_164_2023#environment-variables) in the `.env` file. You can use the following command to edit the file:

```shell
nano .env
```

Change, if needed, the `besson_ethan_info_1a.sql` file in the `database` directory. You can use the following command to edit the file:

```shell
cd FlaskWebS/database
```
```shell
nano besson_ethan_info_1a.sql
```

Return to the root folder of the project and start the server using the following command:

```shell
chmod u+x ./start.sh
```
```shell
./start.sh
```

#### Installation tutorial for linux :
![Linux install](https://raw.githubusercontent.com/InstaZDLL/Besson_Ethan_info1a_164_2023/965beba426ba79254121e839f498331c54fec2b9/.github/Linux_install_tutorial.gif)


## Environment Variables


To run this project, you will need to modify the following environment variables to your `.env` file

`USER_MYSQL` 

`PASS_MYSQL`

`NAME_BD_MYSQL`

`NAME_FILE_DUMP_SQL_BD`

`SELECT_QUERY_ENABLED` - Optional, options : true or false ℹ️

ℹ️ This variable is used to show a table from the database, to see if the SQL dump import was successful.


![Screenshot](https://raw.githubusercontent.com/InstaZDLL/Besson_Ethan_info1a_164_2023/main/.github/Screenshot.png)


## Usage/Examples


#### Qtagselect Usage

To use qtagselect if you want to change the category of the item you've selected, you need to click on the x to remove the actuall, and then select another in the label box.


**Animated tutorial :**

![Qtagselect](https://raw.githubusercontent.com/InstaZDLL/Besson_Ethan_info1a_164_2023/main/.github/Qtagselect_demo.gif)

***

#### SQL Request modifications :

You can change the SQL request to show an other table.

```python
@bp.route('/materiel')
def materiel():
    """
    Retrieves the data from the table t_materiel in the MySQL database and displays it on the page "materiel.html".
    """
    query = "SELECT * FROM t_materiel" # Modify with your query here
    cursor.execute(query)
    data = cursor.fetchall()

    return render_template('materiel.html', data=data)
```

If you change something here don't forget to modify the html code too in the `materiel.html`, or you can also opt for automatic headers such as `marques.html`.

Note : if you change a request in some case you need to change the js and the form to request so that the information is properly handeled.


## Lessons Learned


```text
1. Be specific when asking questions to get the most helpful answers.

2. Use clear and concise language to convey your message effectively.

3. Always backup your important files and documents to avoid losing them.

4. Stay up-to-date with the latest technology trends and tools to improve your productivity.

5. Take breaks and prioritize self-care to avoid burnout.

6. Learning is a lifelong process, and it's important to continually seek knowledge and growth.
````


## Author


- [@InstaZDLL](https://github.com/InstaZDLL)


## License


```text
Copyright (C) 2023 Ethan Besson

Licensed under the Academic Free License version 3.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://opensource.org/license/afl-3-0-php/

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
