"use strict";


// 1. printIndices
function printIndices(items) {
  // Replace this with your code
  for (const item in items){
    console.log (`${items[item]} is at index ${item}`);
  }
}


// 2. everyOtherItem
function everyOtherItem(items) {
  // Replace this with your code
  const listOfEveryOtherItems = []

  for (const item in items){
    if (item % 2 === 0){
      listOfEveryOtherItems.push(items[item])
    }
  }
  console.log(listOfEveryOtherItems)
}


// 3. smallestNItems
function smallestNItems(items, n) {
  // Replace this with your code
  const sortedItems = items.sort((a, b) => a - b);
  sortedItems.slice(0, n);
  const result = sortedItems.reverse();
  
  console.log(result)
}
