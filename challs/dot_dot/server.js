'use strict';

require('dotenv').config(); // load process.env with .env contents
const express = require('express');
const fs = require('fs');

const PORT = 8080;
const HOST = '0.0.0.0';
const API_KEY = process.env.FLAG; // super secret!

const HEADER = `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<!-- Bootstrap CSS -->
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<title>My Homepage</title>
</head>
<body style="margin-top: 5rem;">`;
const FOOTER = `
<!-- Bootstrap JS -->
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
`;

const app = express();
app.get('/', (req, res) => {
    const page = (req.query.page || 'index.html');
    if (new RegExp('^\\.\\.').test(page)) {
	res.status(403).send('Sketchy /^\\.\\./ not allowed!');
    }
    const path = 'content/' + page;
    try {
	const data = fs.readFileSync(path, 'utf8');
	res.send(HEADER + data + FOOTER);
    } catch(err) {
	console.log(err);
	res.status(500).send(err);
    }
});

app.listen(PORT, HOST);
