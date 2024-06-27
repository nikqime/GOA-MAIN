const names = ["ანა", "გიორგი", "სოფო", "მარიამი", "ლევანი", "თამარი", "ნინო", "დავით", "ეკატერინე", "მიხეილი"];
const evenIndexNames = [];

for (let i = 0; i < names.length; i += 2) {
  evenIndexNames.push(names[i]);
}

console.log(evenIndexNames);