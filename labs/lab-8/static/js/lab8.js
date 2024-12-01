/****************************************************************************************************************/
/* In-Class Exercises                                                                                           */
/****************************************************************************************************************/
/* 1. create an array called "fruits" and assign the values "Strawberry", "Raspberry", and "Apple" to it         */
let fruits = []
fruits =["Strawberry", "Raspberry", "Apple"];

/* 2. add two more fruits to the "fruits" array using the correct array method                                   */
fruits.push("Banana", "Orange");
console.log(fruits);

/* 3. sort the fruits array alphabetically using the correct array method                                        */
console.log(fruits.sort());

/* 4. create a function called printFruit that prints each item in the fruits array to the console              */
/*    and call the printFruit function                                                                          */
function printFruit() {
    for (let i = 0; i < fruits.length; i++) {
        console.log(fruits[i]);
    }
}

printFruit();

/* 5. create a fruit class that has three properties: name, color, and season and one method: printFruit()      */
/*    that prints all three properties of the fruit to the console. Then, create 3 fruit objects and print      */
/*    them using the printFruit() method             */
class Fruit {
    constructor(name, color, season) {
        this.name = name;
        this.color = color;
        this.season = season;
    }

    printFruit() {
        console.log(`Name: ${this.name}, Color: ${this.color}, Season: ${this.season}`);
    }
}

const strawberry = new Fruit("Strawberry", "Red", "Spring");
const banana = new Fruit("Banana", "Yellow", "Summer");
const apple = new Fruit("Apple", "Green", "Fall");

strawberry.printFruit();
banana.printFruit();
apple.printFruit();

/****************************************************************************************************************/
/* In-Class Lab                                                                                                 */
/****************************************************************************************************************/
/* 1. Write a function that asks the user if they want to say hi. If the user selects "Okay" (true), then       */
/*    display a welcome message. If the user selects "Cancel" (false), then display a different message         */
function areYouSure() {
    const welcomeElement = document.getElementById("welcome");
    const userResponse = confirm("Would you like to say hi?");
    
    if (userResponse) {
        welcomeElement.textContent = "Welcome! Thanks for saying hi!";
    } else {
        welcomeElement.textContent = "Maybe next time!";
    }
}

/* 2. Write a function to change 3 styles on the webpage                                                        */
function changeStyle() {
    document.getElementById("welcome").style.color = "green";
    document.querySelector("button").style.backgroundColor = "cyan";
    document.querySelector("div").style.backgroundColor = "blue";
}
