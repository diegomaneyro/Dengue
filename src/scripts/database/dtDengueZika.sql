/*Borar database*/
DROP DATABASE `biex6hbtttobycu0rvjz`;
CREATE DATABASE IF NOT EXISTS `biex6hbtttobycu0rvjz`;
USE `biex6hbtttobycu0rvjz`;

/*Crear tablas*/
CREATE TABLE CasosDengue (
	id INT(30) NOT NULL AUTO_INCREMENT,
    año INT(30),
    semana INT(30),
    provincia VARCHAR(50),
    localidad varchar(50),
    latitud INT(50),
    longitud INT(50),
    cantidadCasos INT(180),
    PRIMARY KEY (id)
    );

CREATE TABLE CasosZika (
	id INT(30) NOT NULL AUTO_INCREMENT,
    año INT(30),
    semana INT(30),
    provincia VARCHAR(50),
    localildad varchar(50),
    latitud INT(50),
    longitud INT(50),
    cantidadCasos INT(180),
    PRIMARY KEY (id)    
	);
    
CREATE TABLE UltimosCasos (
	id INT NOT NULL AUTO_INCREMENT,
    año INT(30),
    semana INT(30),
    provincia VARCHAR(50),
    evento VARCHAR(80),
    cantidadCasos INT(180),
    PRIMARY KEY (id)
    ); 



    

