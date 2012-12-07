function recup_extension(fichier) // fonction de récupération extension fichier
   {
         if (fichier!="")// si le champ fihier n'est pas vide
         {
            nom_fichier=fichier;// on récupere le chemin complet du fichier
            nbchar = nom_fichier.length;// on compte le nombre de caractere que compose ce chemin
            extension = nom_fichier.substring(nbchar-4,nbchar); // on récupere les 4 derniers caracteres
            extension=extension.toLowerCase(); //on uniforme les caracteres en minuscules au cas ou cela aurait été écris en majuscule...
            return extension; // on renvoi l'extension vers la fonction appelante
         }
   }

function verif_extension(fichier)// fonction vérification de l'extension aprés avoir choisi le fichier
   {
   ext = recup_extension(fichier);// on appelle la fonction de récupération de l'extension et on récupere l'extension
   
            if(ext==".jpg"||ext==".svg"||ext==".png"){}// si extension = a une des extension suivante alors tout est ok donc ... pas d'erreur
            else // sinon on alert l'user de la mauvaise extension
            {
               alert("L'extension du fichier que vous voulez uploader est :'"+extension+"'\n cette extension n'est pas autorisée !\n Seules les extesnions suivantes sont autorisées :\n'JPG;PNG;SVG' !");
            }
   }

function verif_before_valid_form()// fonction de validation de formulaire
   {
      var msgerr="Veuillez vérifier les erreurs suivantes :\n";// préparation message d'erreur 
      var erreur = 0;// par defaut tout est ok
      
      if(document.transfert_file.ajout_fichier.value!="")// si le champ fihier n'est pas vide
      {
               ext = recup_extension(document.transfert_file.ajout_fichier.value);// on appelle la fonction de récupération de l'extension et on récupere l'extension
               
               if(ext==".jpg"||ext==".svg"||ext==".png"){} // si extension = a une des extension suivante alors tout est ok donc ... pas d'erreur
               else // sinon message d'erreur
               {
                  msgerr=msgerr+"- L'extension du fichier n'est pas valide, les extensions acceptées sont 'JPG;PNG;SVG' ! \n";// prépare message d'erreur
                  erreur = 1;// il y a une erreur donc on l'informe
               }
      }
   
   if(erreur==1)
      {
         alert(msgerr);
      }
   else
      {
         transfert_file.submit();
      }
}
