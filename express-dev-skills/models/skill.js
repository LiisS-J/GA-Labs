const skills = [
    {skill: 'Creating a simple browser game', accomplished: true},
    {skill: 'Styling in CSS', accomplished: true},
    {skill: 'General understanging of Javascript', accomplished: true},
    {skill: 'Searching Google for answers', accomplished: false},
    {skill: 'Doubting ones abilities as a developer at least 2x a day', accomplished: true},
    {skill: 'General understanding of Express framework', accomplished: true}
];
  
module.exports = {
   getAll,
   getOne,
   create,
   deleteOne,
   update
};

function update(id, skill) {
    skills.splice(id, 1, skill);
}

function getAll() {
    return skills;
}

function getOne(id) {
    return skills[id];
}

function create(skill) {
    skills.push(skill);
}

function deleteOne(id){
    skills.splice(id, 1);
}