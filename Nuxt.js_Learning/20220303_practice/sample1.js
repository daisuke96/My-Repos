const person = {
    myNumber : 1000,
    email : 'john.smith@dev.com',
    personalInfo:{
        firstName : 'John',
        lastName : 'Smith',
        age : 30,
        fullName : function(){
            return this.firstName + " " + this.lastName;
        }
    }
}

console.log(person.personalInfo.age);
console.log(person.personalInfo.fullName());
