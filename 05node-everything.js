
console.log('hello xxxx\n');
//console.log('');

//------------    : sign     ---------------

//create object in a classic way

var warrior = {
	name: 'Conan',
	weapon: 'sword'
}

console.log('The warrior is named ' + warrior.name + ' and his weapon is ' + warrior.weapon +  '.');

var warrior2 = new Object();
warrior2.name = 'Spartacus'
warrior2.weapon = 'Axe'

console.log('The second warrior is named ' + warrior2.name + ' and his weapon is ' + warrior2.weapon +  '.');

console.log('\n');
//------------------------------------------


		/*
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
		*/