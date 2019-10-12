// Client-side javascript
// Link: https://ruxpert.ru/%D0%A1%D1%83%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D1%8B_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B9%D1%81%D0%BA%D0%BE%D0%B9_%D0%A4%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8


// Prepare
let allSubjsData = [];
let allSubjs = $('tbody')[1].children;
String.prototype.replaceAll = function(search, replace){
  return this.split(search).join(replace);
}

// Actions
for(let i = 0; i < allSubjs.length; i++) {
	// Getting values
	let currSubjName = allSubjs[i].children[1].children[0].innerHTML.replaceAll('\n', '');
	let currPopulation = 0;//parseInt(allSubjs[i].children[3].innerHTML.replaceAll(' ', ''));
	let currCapitalCityName = allSubjs[i].children[6].children[0].innerHTML.replaceAll('\n', '');
	let currFederalDistrict = allSubjs[i].children[7].innerHTML.replaceAll('\n', '');

	if (currSubjName == "Россия")
		continue;
	allSubjsData.push({
    "name": currSubjName,
    //"population": currPopulation,
    "capitalCityName": currCapitalCityName,
    "federalDistrict": currFederalDistrict
	});
}

console.log(JSON.stringify(allSubjsData));