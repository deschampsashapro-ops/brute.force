




const ecran = document.getElementById("ecran");
const boutons = document.querySelectorAll("button");
const boutonEgal = document.getElementById("egal");
const boutonClear = document.getElementById("clear");
const boutonPi = document.getElementById("pi");
const boutonRacine = document.getElementById("racine")
const boutonPuissance = document.getElementById("puissance")

// Ajouter les chiffres et opérateurs
boutons.forEach(bouton => {
    bouton.addEventListener("click", () => {
        const valeur = bouton.getAttribute("data-val");
        if (valeur) {
            ecran.value += valeur;
        }
    });
});

//Pi
boutonPi.addEventListener("click", function () {
    ecran.value += Math.PI;
    console.log(Math.PI);
});

//Racine carre
boutonRacine.addEventListener("click", function () {
    if (ecran.value !== "") {
        ecran.value = Math.sqrt(parseFloat(ecran.value));
    }
});

//Puissance
boutonPuissance.addEventListener("click", function () {
    if (ecran.value !== "") {
        ecran.value = Math.pow(parseFloat(ecran.value), 2);
    }
})


// Calcul
boutonEgal.addEventListener("click", () => {
    try {
        ecran.value = eval(ecran.value);
    } catch {
        ecran.value = "Erreur";
    }
});

// Effacer
boutonClear.addEventListener("click", () => {
    ecran.value = "";
});