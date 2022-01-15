var myArray = {
    x: {1:50, 2:60, 3:70}, y: {1: 7, 2: 8, 3: 9}
    
};

const getValues=(obj)=>{
emp = []
for(var i=0; i<Object.keys(obj).length; i++){
    var h = Object.values(obj)[i]
    for(let k in h){
        emp.push(h[k])
        
    } 
}
return emp
}

console.log(getValues(myArray))
// a = getValues(myArray)
// for(var i =0; i<a.length; i++){
//     console.log(a[i])
// }
// console.log(h)
// console.log(h.length)

// for(var i=0; i<h.length; i++){
//     console.log(h[i])
// }

// var k = [1, 2, 3]
// v = 1







// var size = Object.keys(myArray).length;
// console.log(size)

// var h = Object.values(myArray)[0]
// console.log(h)

// console.log(myArray.y)


// j = [1, 2, 3]

// console.log(j.length)

// console.log(myArray[0].x['3'])

// f = []

// for(var i =0; i<myArray.y.length; i++){
//     console.log(myArray[i]) 
// }
    
    // console.log(i)
    // f.push(myArray[i]) 
    

// console.log(f)
// console.log(2)

// console.log(myArray[0])