function verifNom() {
  let nom = document.getElementById("nom").value;
  let erreur = document.getElementById("erreur-nom");
  let bouton = document.getElementById("bouton");

  if (nom.includes(',') || nom.length < 3 || nom.length > 20) {
    erreur.style.display = "block";
    bouton.disabled = true;
  } else {
    erreur.style.display = "none";
    bouton.disabled = false;
  }
}

function verifEspece() {
  let espece = document.getElementById("espece").value;
  let erreur = document.getElementById("erreur-espece");
  let bouton = document.getElementById("bouton");

  if (espece.includes(',')) {
    erreur.style.display = "block";
    bouton.disabled = true;
  } else {
    erreur.style.display = "none";
    bouton.disabled = false;
  }
}

function verifRace() {
  let race = document.getElementById("race").value;
  let erreur = document.getElementById("erreur-race");
  let bouton = document.getElementById("bouton");

  if (race.includes(',')) {
    erreur.style.display = "block";
    bouton.disabled = true;
  } else {
    erreur.style.display = "none";
    bouton.disabled = false;
  }
}

function verifAge() {
    let age = document.getElementById("age").value;
    let erreur = document.getElementById("erreur-age");
    let bouton = document.getElementById("bouton");
    let nombrePattern = /^\d+$/;
  
    if (!nombrePattern.test(age) || age < 0 || age > 30) {
      erreur.style.display = "block";
      bouton.disabled = true;
    } else {
      erreur.style.display = "none";
      bouton.disabled = false;
    }
  }

  function verifDescription() {
    let description = document.getElementById("descritpion").value;
    let erreur = document.getElementById("erreur-description");
    let bouton = document.getElementById("bouton");
  
    if (description.includes(',')) {
      erreur.style.display = "block";
      bouton.disabled = true;
    } else {
      erreur.style.display = "none";
      bouton.disabled = false;
    }
  }

  function verifAdresse() {
    let adresse = document.getElementById("adresse").value;
    let erreur = document.getElementById("erreur-adresse");
    let bouton = document.getElementById("bouton");
  
    if (adresse.includes(',')) {
      erreur.style.display = "block";
      bouton.disabled = true;
    } else {
      erreur.style.display = "none";
      bouton.disabled = false;
    }
  }

  function verifVille() {
    let ville = document.getElementById("ville").value;
    let erreur = document.getElementById("erreur-ville");
    let bouton = document.getElementById("bouton");
  
    if (ville.includes(',')) {
      erreur.style.display = "block";
      bouton.disabled = true;
    } else {
      erreur.style.display = "none";
      bouton.disabled = false;
    }
  }

  function verifCp() {
    let cp = document.getElementById("cp").value;
    let erreur = document.getElementById("erreur-cp");
    let bouton = document.getElementById("bouton");
    let pattern = /^[A-Za-z]\d[A-Za-z] \d[A-Za-z]\d$/;
  
    if (cp.includes(',') || !pattern.test(cp)) {
      erreur.style.display = "block";
      bouton.disabled = true;
    } else {
      erreur.style.display = "none";
      bouton.disabled = false;
    }
  }

  function refresh() {
    document.getElementById("formulaire").reset();
    location.reload();
}