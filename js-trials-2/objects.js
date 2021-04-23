"use strict";


// 1. countWords
function countWords(phrase) {
  // Replace this with your code
  const wordCounts = {}

  for (const word of phrase.split(' ')){
    if(wordCounts[word]){
      wordCounts[word] += 1;
    } else{
      wordCounts[word] = 1
    }
  }
  return wordCounts;
}


// 2. getMelonsAtPrice
function getMelonsAtPrice(price) {
  // Replace this with your code
  const melonPrice = {
    2.50: ['Cantaloupe', 'Honeydew'],
    2.95: ['Watermelon'],
    3.25: ['Musk', 'Crenshaw'],
    14.25: ['Christmas'] 
  };
  if(!melonPrice[price]){
    return 
  }
  return melonPrice[price].sort();
}
