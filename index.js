
let characters = ['ELAINE', 'JERRY', 'GEORGE', 'KRAMER', 'NEWMAN'];
document.addEventListener("DOMContentLoaded", () => {
  fetch('./data.json').then((res) => {
    return res.json();
  }).then((data) => {
    d3.select("#graph");
    let xScale = d3.scaleBand()
      .rangeRound([0, window.innerWidth - 20])
      .paddingInner(0.05)
      .domain(data.map((episode) => {return episode["TITLE"]}));

    let yScale = d3.scaleLinear()
      .rangeRound([window.innerHeight, 0])
      .domain([0, d3.max(data, function(d){
        let total = 0;
        Object.keys(d).forEach(key => {
          let num = d[key];
          if(typeof(num) !== 'string'){
            total += num;
          }
        });
        return total;
      })]);
    debugger;
  });
});