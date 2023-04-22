//chart data
window.addEventListener("load", (event) => {
    options.body = JSON.stringify({
        id: getCookie("id")
    })
    fetch("/film/getavgstars", options).then(response => response.json())
        .then(response => {

            var chartjson = {
                "data": response,
                "xtitle": "Secured Marks",
                "ytitle": "Marks",
                "ymax": 100,
                "ykey": 'score',
                "prefix": "%"
            }


            //constants
            var TROW = 'tr',
                TDATA = 'td';

            var chart = document.createElement('div');
            //create the chart canvas
            var barchart = document.createElement('table');
            //make the colspan to number of records

            //create the bar row
            var barrow = document.createElement(TROW);

            //lets add data to the chart
            for (var i = 0; i < chartjson.data.length; i++) {
                barrow.setAttribute('class', 'bars');
                var prefix = chartjson.prefix || '';
                //create the bar data
                var bardata = document.createElement(TDATA);
                var bar = document.createElement('div');
                bar.setAttribute('class', "bg-letterboxd-3");
                bar.classList.add("border");
                bar.classList.add("border-black");
                bar.style.height = chartjson.data[i][chartjson.ykey] + prefix;

                bardata.appendChild(bar);
                barrow.appendChild(bardata);

            }



            barchart.appendChild(barrow);
            chart.appendChild(barchart);
            document.getElementById('chart').innerHTML = chart.outerHTML;



        });

});