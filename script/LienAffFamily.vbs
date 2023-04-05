' Importation de la bibliothèque pour ouvrir un navigateur web
Set wshShell = WScript.CreateObject("WScript.Shell")

' Message d'accueil pour l'utilisateur
message = "========== Amazon pour la famille ==========" & vbCrLf _
        & "1. Entrez le produit que vous recherchez" & vbCrLf _
        & "2. Choisissez Oui pour ouvrir le lien Amazon" & vbCrLf _
        & "3. Si vous achetez dans les 24 heures, j'aurai une commission" & vbCrLf _
        & "4. Cela ne change rien pour vous" & vbCrLf _
        & "5. Merci pour votre soutien"

' Affichage des options dans une seule MsgBox
reponse = MsgBox(message, vbOKCancel)

' Si l'utilisateur choisit "OK", demande le produit recherché
If reponse = vbOK Then
    product = InputBox("Quel produit recherchez-vous?")
    ' Construction de l'URL de recherche sur Amazon
    url = "https://www.amazon.fr/s?k="
    lienAff = "&tag=price-comberu-21"
' le lien aff ne reste pas dans l'url lorsque l'utilisateur clique sur le produit!'
'https://www.amazon.fr?&linkCode=ll2&tag=price-comberu-21&linkId=2c3c31b24db0f154704ad6b3e0e7fab8&language=fr_FR&ref_=as_li_ss_tl'


    ' Demande à l'utilisateur s'il veut ouvrir la page web Amazon
    reponse_web = MsgBox("Voulez-vous ouvrir la page web ? oui / non", vbYesNo)

    ' Si l'utilisateur choisit "Oui", ouvre la page web Amazon dans le navigateur
    If reponse_web = vbYes Then
        wshShell.Run(url & product & lienAff)
    ' Si l'utilisateur choisit "Non", affiche un message de remerciement
    ElseIf reponse_web = vbNo Then
        WScript.Echo "Vous avez choisi de ne pas ouvrir de page web. Bonne journée."
    ' Si l'utilisateur entre une réponse invalide, affiche un message d'erreur
    Else
        WScript.Echo "Je ne comprends pas votre réponse."
    End If
' Si l'utilisateur choisit "Annuler", quitte le programme
ElseIf reponse = vbCancel Then
    WScript.Quit
End If

' Pause pour donner à l'utilisateur le temps de lire le résultat
WScript.Sleep 1000

