let dragon = 
// dragon is a function that takes a name
    name =>
    //it will return another function which is size
        size =>
        //function size will return functino element
            element =>
            //function element will return string
            name + ' is a ' +
            size + ' dragon that breathes ' +
            element + ' ! '

console.log(dragon('fluffy ')('tiny ')('lightning '))