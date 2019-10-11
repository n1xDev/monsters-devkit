// Client-side javascript
// Link: https://ru.wikipedia.org/wiki/%D0%9D%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5_%D1%81%D1%83%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%BE%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B9%D1%81%D0%BA%D0%BE%D0%B9_%D0%A4%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8


// Prepare
let allSubjsData = [];
let allSubjs = $('table.standard.sortable.jquery-tablesorter')[0].children[1].children;
String.prototype.replaceAll = function(search, replace){
  return this.split(search).join(replace);
}

// Actions
for(let i = 0; i < allSubjs.length; i++) {
	// Getting values
	let currSubjName = $('table.standard.sortable.jquery-tablesorter')[0].children[1].children[i].children[1].children[0].innerHTML.replaceAll('<br>', '/');
	let currPopulationCount = parseInt($('table.standard.sortable.jquery-tablesorter')[0].children[1].children[i].children[2].innerHTML.replaceAll(',', '.'));
	let currPercentOfSummaryCountryPopulation = parseFloat($('table.standard.sortable.jquery-tablesorter')[0].children[1].children[i].children[3].innerHTML.replaceAll(',', '.'));
	let currArea = parseInt($('table.standard.sortable.jquery-tablesorter')[0].children[1].children[i].children[8].innerHTML.replaceAll(',', '.'));

	// Skipping drafts
	//if (currSubjName.indexOf('РФ') > -1 || currSubjName.indexOf('Архангельская область без НАО') > -1)
	//	continue;

	allSubjsData.push({
		"name": currSubjName,
		"populationCount": currPopulationCount,
		"area": currArea,
		"percentOfSummaryCountryPopulation": currPercentOfSummaryCountryPopulation
	});
}

console.log(JSON.stringify(allSubjsData));