$(document).ready(function() {
    // Sélectionnez l'élément dans lequel vous souhaitez charger le contenu du fichier HTML
    var graphContainer = $('#graph-container4');

    // Faites une requête AJAX pour charger le contenu du fichier HTML
    $.ajax({
        url: 'templates/graph/graph4.html',  // Remplacez par le chemin relatif ou absolu vers votre fichier HTML
        type: 'GET',
        dataType: 'html',
        success: function(response) {
            // Chargez le contenu du fichier HTML dans l'élément graphContainer
            graphContainer.html(response);
        },
        error: function(xhr, status, error) {
            console.error(error);
        }
    });
});
