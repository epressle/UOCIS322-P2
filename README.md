# UOCIS322 - Project 2 - Ethan Pressley, epressle@uoregon.edu #

A "getting started with Docker" project that incorperates the same file checks as project 1, but with Flask and Docker.


NOTE: This project requires Docker.  
NOTE 2: This project's docroot is web/pages/, and templates is web/templates/.

## Getting started

* Build the simple flask app image using

  ```
  docker build -t your-name-cis322-2 .
  ```
* Run the container using

  ```
  docker run -d -p <someport>:5000 your-name-cis322-2
  ```
NOTE: Make sure to specify a free port for <someport>.
* Launch `http://hostname:<someport>` using your web browser and it should output "UOCIS docker demo!".

* Stop the container using

  ```
  docker stop <container-ID>
  ```

## Tasks

* The goal of this project is to implement the same "file checking" logic that you implemented in Project 1, but using Flask.

* Like Project 1, if a file (`docroot/name.extension`, any name, any extention or format) exists, transmit `200/OK` header followed by that file html. If the file doesn't exist, transmit an error code in the header along with the appropriate page html in the body. You'll do this by creating error handlers that will be (or are) taught in class (refer to the recordings if needed). You'll also create the following two html files with the error messages:
    * `404.html` will display "File not found!"
    * `403.html` will display "File is forbidden!"

    ⚠️ NOTE: if a request contains illegal characters (// .. ~) anywhere (not just the beginning), the response should be 403.
    
    ⚠️ NOTE: it's okay if `//` doesn't work if it's at the beginning of the request since Flask will remove those.
