let array= new Array(1, 2, 3, 4, 5 , 89);
array[1] = 69;
console.log(array[2]); 
array.push(6);

array.pop();
array.pop();
array.pop();
array.pop();
array.pop();

console.log(array); 


let arrayLiteral = [10, 20, 30, 40, 50];
arrayLiteral[4] = 200;
console.log(arrayLiteral[3]); 
arrayLiteral.push(60);
arrayLiteral.pop();
arrayLiteral.pop();
arrayLiteral.pop();
arrayLiteral.pop();

console.log(arrayLiteral);


let shecdoma = [1,2,3,4,69,1488];
shecdoma[1]=23;
shecdoma[3]=41;
shecdoma[6]=23114114 ; /*ეს შეცდომაა რადგან მეექვსე არ გვაქვს*/ //undefined//
console.log(shecdoma)