'use strict';

function getBookName(nik, ht, no) { // nik is nikaya, ht is a DPR_G.G_hier, no will be xml no - 1


  if (nik == 'k' || nik == 'y') {
    no = DPR_G.G_kynames[nik][no];
    if(ht != 'm') no = no.replace(/([^a]) 1$/,'$1');
  }
  else no++;
  return no.toString();
}


function getDppnEntry(term) {
  if(typeof(DPR_G.D) == 'undefined')
    addJS(['dppn']);
  var dppnEntry = [];
  if(typeof(DPR_G.D[term]) == 'object') {
    dppnEntry = DPR_G.D[term];
  }
  else {
    if(typeof(DPR_G.D[term.replace(/\.m$/,'')]) == 'object') {
      dppnEntry = DPR_G.D[term.replace(/\.m$/,'')];
    }
    else if(typeof(DPR_G.D[term.replace(/o$/,'a')]) == 'object') {
      dppnEntry = DPR_G.D[term.replace(/o$/,'a')];
    }
  }
  var dEI = [];
  if(dppnEntry.length > 0) {
    for(var d in dppnEntry) {
      dEI.push(dppnEntry[d]);
    }
  }
  return dEI;
}
