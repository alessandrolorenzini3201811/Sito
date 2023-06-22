
document.addEventListener('DOMContentLoaded', function () {
    var jsonPath ='http://3.72.77.8:5000/'; // Imposta il percorso del file JSON

    fetchJSON(jsonPath)
        .then(json => {
            initializeCytoscape(json);
        })
        .catch(error => {
            console.error('Error fetching JSON:', error);
        });

function fetchJSON(jsonPath) {
    return fetch(jsonPath)
        .then(response => response.json());
}
 
function initializeCytoscape(json) {
    console.log(json);
    var cy = cytoscape({
        
        container: document.getElementById('cy'),
        elements:{
            nodes: json.nodes,
            edges: json.edges
          },
        style: [
            {
                selector: 'node',
                style: {
                    'label': 'data(label)',
                    'background-color': 'data(justified)',
                    'width': '40px',
                    'height': '40px',
                    'border-color': '#000',
                    'border-width': '2px',
                    'border-opacity': '1',
                    'text-valign': 'center',
                    'color': '#fff',
                    'text-outline-color': '#000',
                    'text-outline-width': '1px',
                    'text-outline-opacity': '1',
                    'content': 'data(id)',
                    'text-wrap': 'wrap',
                    'text-max-width': '40px',
                    'text-justification': 'center'
                }
            },
            {
                selector: 'edge',
                style: {
                    'width': 2,
                    'line-color': 'data(color)',
                    'target-arrow-color': 'data(color)',
                    'target-arrow-shape': 'triangle',
                    'curve-style': 'bezier',
                    'control-point-step-size': 40
                }
            },
            {
                selector: '.highlighted',
                style: {
                    'opacity': '1'
                }
            },
            {
                selector: '.faded',
                style: {
                    'opacity': '0.2'
                }
            }
        ],
        layout: {
            name: 'random'
        }
    });

    var selectedElements = cy.collection();

    cy.on('tap', 'node', function (event) {
        var node = event.target;
        var neighborhood = node.closedNeighborhood();

        selectedElements.removeClass('highlighted');
        selectedElements = neighborhood;
        selectedElements.addClass('highlighted');
        cy.elements().difference(selectedElements).addClass('faded');
    });

    cy.on('tap', function (event) {
        if (event.target === cy) {
            selectedElements.removeClass('highlighted faded');
        }
    });
}
});
