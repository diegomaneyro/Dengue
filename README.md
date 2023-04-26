# Dengue y Zika en Argentina

Casos de Dengue y Zika en Argentina 2022, registrados por provincia y departamento.


## Objetivos del Proyecto

 - [ETL y EDA de los datasets](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Dashboar y reporte](https://github.com/matiassingers/awesome-readme)
 - [Modelo de Machine Learning](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)


## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### Objetivo de la api:

Querys por provincia, distrito y mes. retorna cantidad de casos.


## Authors

- [Diego Maneyro](https://www.github.com/octokatherine)


## Deployment

deploy de la api para las consultas desde IBM Cloud

```bash
  npm run deploy
```


