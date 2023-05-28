# FlaskWebS


This is a simple web application created as part of the Modulus 164 project. 

The goal of this project is to show our skills and understanding of web development.


[![Version](https://img.shields.io/github/v/release/InstaZDLL/Besson_Ethan_info1a_164_2023?style=for-the-badge)](https://github.com/InstaZDLL/Besson_Ethan_info1a_164_2023/releases)
[![AFLv3 License](https://img.shields.io/github/license/InstaZDLL/Besson_Ethan_info1a_164_2023?logo=e&style=for-the-badge)](https://opensource.org/license/afl-3-0-php)
[![Last commit](https://img.shields.io/github/last-commit/InstaZDLL/Besson_Ethan_info1a_164_2023?style=for-the-badge)](https://github.com/InstaZDLL/Besson_Ethan_info1a_164_2023/commits/main)


[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)


## Roadmap


1. [x] Add the option to modify the content of a table in the `marques.html`.
2. [x] Add the option to add content to the table in the `marques.html`.
3. [x] Correct the code of the delete button in the `marques.html` and modify the `main.py` for create the sql request.
4. [ ] ~~Add the option to recover button for restoring the previous database.~~
5. [ ] Add an image in the footer.
6. [ ] Add functionality to the filter button in `materiel.html`.
7. [x] Add a tag table to the editing panel. 🔄
8. [x] Add functionality to the two remaining buttons in `categorie.html`.
9. [x] Restructuring of file names and paths. 🔜
10. [x] Re-structuring of the sources of the html files and optimization of the code.
11. [x] Add protection against SQL injections.
12. [x] Separate the different app routes in separate files for a better organization of the code.
13. [x] Import automatically the database when the server starts.
14. [x] Add a `run-app.py` file and initialize the application package in it. 🔄
15. [x] Removal of unused fonts in `/fonts` folder.
16. [ ] Add functionality to the `/success` app route.
17. [ ] Add a success and a failed popup when submitting to all forms linked to `categorie.html`. 🔄
18. [ ] Add the possibility to change the id of the marques in all linked forms in the `marques.html`.
19. [x] Correct all resource paths.
20. [x] Fix the bug of the qtagselect from the page `modify_materiel.html`.
21. [x] Move the database SQL and the `mysql_dump_import.py` to a python package.
22. [x] Implement the functionality to import the database in the `run_app.py`.
23. [x] Add a switch en the `.env` file to display or not the connection test result table. 🔄
24. [x] Fix the error when the starting the run_app.py: `1049 (42000): Unknown database`. 🔄
25. [ ] Handle all mysql exceptions in a separate file in the `/database` package with a specific custom message. 🔜


### Definitions :


1. [x] Finished
2. [ ] In progress
3. [ ] ~~Cancelled~~

- 🔄 The objective has been modified (not the original but keep the same goal)
- 🔜 The objective is partially completed (with further updates to come)

## Run Locally

### Windows

Clone the project.

```git
git clone https://github.com/InstaZDLL/Besson_Ethan_info1a_164_2023.git
```

Go to the project directory.

```shell
cd Besson_Ethan_info1a_164_2023
```

Modify the [environment variables](https://github.com/InstaZDLL/Besson_Ethan_info1a_164_2023#environment-variables) in the `.env` file. You can edit the file with Notepad or another text editing tool.

```shell
notepad .env
```

Change, **if needed**, the `besson_ethan_info_1a.sql` file in the `database` directory. You can edit the file with Notepad or another text editing tool.

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

### Linux

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
./start.sh
```


## Environment Variables


To run this project, you will need to modify the following environment variables to your `.env` file

`USER_MYSQL` 

`PASS_MYSQL`

`NAME_BD_MYSQL`

`NAME_FILE_DUMP_SQL_BD`

`SELECT_QUERY_ENABLED` - Optional, options : true or false ℹ️

ℹ️ This variable is used to show a table from the database, to see if the SQL dump import was successful.


![Screenshot](https://raw.githubusercontent.com/InstaZDLL/Besson_Ethan_info1a_164_2023/working-channel/.github/Screenshot.png)


## Usage/Examples


You can change the sql request to show an other table.

```python
@bp.route('/marques')
def marques():
    """
    Retrieves the data from the t_brand table in the MySQL database and displays it on the "brands.html" page.
    """
    query = """
        SELECT t_marque.id_marque, t_marque.nom_marque, description_marque
        FROM t_marque
        WHERE t_marque.id_marque;
    """
    cursor.execute(query)
    data = cursor.fetchall()

    headers = [column[0] for column in cursor.description]

    return render_template('marques.html', data=data, headers=headers)
```

If you change something here don't forget to modify the html code too in the `personnes.html`, or you can also opt for automatic headers such as `marques.html`.


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
