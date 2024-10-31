// Receber a entrada do usuário
let frase = prompt("Digite uma palavra ou frase:");

// Limpar a frase
let fraseLimpa = frase
  .toLowerCase()           // Converte todas as letras para minúsculas
  .replace(/[^a-z0-9]/g, ""); // Remove tudo que não é letra ou número

// Verificar se é um palíndromo
if (fraseLimpa === fraseLimpa.split("").reverse().join("")) {
  console.log("É um palíndromo!");
} else {
  console.log("Não é um palíndromo.");
}
