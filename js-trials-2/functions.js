"use strict";


// 1. isHometown

// Define your function here
function isHometown(town){
    // bool: True if `town` is 'San Francisco'
    return town === "San Francisco";
}
        


// 2. getFullName

// Define your function here
function getFullName(firstName, lastName){
    return `${firstName} ${lastName}`
}

// 3. calculateTotal

// Define your function here
function calculateTotal(basePrice, state, tax=0.05){
    const subtotal = basePrice * (1 + tax);
    let fee = 0;
    
    if (state === 'CA'){
        fee = 0.03 * subtotal;
    } else if (state === 'PA'){
        fee = 2;
    } else if (state === 'MA'){
        if (basePrice <= 100){
            fee = 1;
        } else {
            fee = 3;
        }
    }
    return subtotal + fee
}
