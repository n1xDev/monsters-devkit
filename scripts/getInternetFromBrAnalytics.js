// Client-side javascript
// Link: https://br-analytics.ru/statistics/am/?hub_id=2&date=201909&period_type=month

// Prepare
let allSubjsData = [];
let allSubjs = $('tbody')[0].children;
String.prototype.replaceAll = function(search, replace){
  return this.split(search).join(replace);
}

// Actions
for(let i = 1; i < allSubjs.length; i++) {
	// Getting values
	let currSubjName = allSubjs[i].children[1].innerHTML;
	let currPopulation = parseInt(allSubjs[i].children[3].innerHTML.replaceAll(' ', ''));
	let currPenetrationPercentage = parseFloat(allSubjs[i].children[4].innerHTML.replaceAll(' ', '').replaceAll('%', ''));
	let currSocialPostsAuthorsCount = parseInt(allSubjs[i].children[2].innerHTML.replaceAll(' ', ''));

	allSubjsData.push({
    "name": currSubjName,
    "population": currPopulation,
    "penetrationPercentage": currPenetrationPercentage,
    "socialPostsAuthorsCount": currSocialPostsAuthorsCount
	});
}

console.log(JSON.stringify(allSubjsData));