//https://www.amazon.fr/s?k=ensemble+homme

import cheerio from 'cheerio'
//import nodeFetch from 'node-fetch'

const cheerio = require('cheerio');
//const fetch = require('node-fetch');

// function to get the raw data
function getRawData(URL) {
   return fetch(URL)
      .then((response) => response.text())
      .then((data) => {
         return data;
      });
}

// URL for data
const URL = "https://en.wikipedia.org/wiki/Cricket_World_Cup";

// start of the program
const getCricketWorldCupsList = async () => {
   const cricketWorldCupRawData = await getRawData(URL);

   // parsing the data
   const parsedCricketWorldCupData = cheerio.load(cricketWorldCupRawData);

   // extracting the table data
   const worldCupsDataTable = parsedCricketWorldCupData("table.wikitable")[0]
      .children[1].children;

   console.log("Year --- Winner --- Runner");
   worldCupsDataTable.forEach((row) => {
      // extracting `td` tags
      if (row.name === "tr") {
         let year = null,
            winner = null,
            runner = null;

         const columns = row.children.filter((column) => column.name === "td");

         // extracting year
         const yearColumn = columns[0];
         if (yearColumn) {
            year = yearColumn.children[0];
            if (year) {
               year = year.children[0].data;
            }
         }

         // extracting winner
         const winnerColumn = columns[3];
         if (winnerColumn) {
            winner = winnerColumn.children[1];
            if (winner) {
               winner = winner.children[0].data;
            }
         }

         // extracting runner
         const runnerColumn = columns[5];
         if (runnerColumn) {
            runner = runnerColumn.children[1];
            if (runner) {
               runner = runner.children[0].data;
            }
         }

         if (year && winner && runner) {
            console.log(`${year} --- ${winner} --- ${runner}`);
         }
      }
   });
};

// invoking the main function
getCricketWorldCupsList();
