//https://www.programasaudefacil.com.br/calculadora-de-imc

//O site possui o botão de calcular onde é ativado com o click e cria o background de cor diferente para a área que o IMC está relacionado.

document.getElementById('submit_calc').onclick=function(){var altura=document.getElementById('altura_input').value.replace('.','').replace(',','.');
var peso=document.getElementById('peso_input').value.replace('.','').replace(',','.');
var imc=parseFloat((peso/(altura*altura)).toFixed(2));
if(altura&&peso){document.querySelector('.calc-result strong').innerHTML=imc;
$("html,body").animate({scrollTop:($(".table-calc").offset().top-30)});var eq_result;
if(imc<18.5){eq_result="0";}else if(imc>18.5&&imc<25){eq_result="1";}
else if(imc>25&&imc<30){eq_result="2";}
else if(imc>30&&imc<40){eq_result="3";}
else if(imc>40){eq_result="4";}
$(".table-calc tbody tr").css({backgroundColor:"#fff"});
$("#result_calc_"+eq_result).css({backgroundColor:"#ebfdea"});}
else{document.querySelector('.calc-result strong').innerHTML="";
$(".table-calc tbody tr").css({backgroundColor:"#fff"});}}
document.getElementById('clear_calc').onclick=function(){document.getElementById('altura_input').value="";
document.getElementById('peso_input').value="";document.querySelector('.calc-result strong').innerHTML='';
$(".table-calc tbody tr").css({backgroundColor:"#fff"});
}}})
$(function(){var extlink='';
$('.ext-link').click(function(e){e.preventDefault();
extlink=$(this).attr('href');$('#modal').css('display','block');});$('#modal-cancel').click(function(){$('#modal').css('display','none');});$('#modal-continue').click(function(){window.open(extlink,'_blank');$('#modal').css('display','none');});});


//https://www.acaidapraca.com/webapp/globais/cardapio/F9Z1DM
//O botão adiciona o elemento ao carrinho de compras através do "onclick".
<a href="javascript: itens.modal(272999);" onclick="if(typeof fbq === 'function'){ fbq('track', 'ViewContent', { content_name: 'Combo - 500ml + 8 Acompanhamentos | SKU-Z7UU86', currency: 'BRL', value: 12.00 }); } if(typeof gtag === 'function'){ gtag('event', 'view_item', {'currency':'BRL','items':[{'item_id':'Z7UU86','item_name':'Combo - 500ml + 8 Acompanhamentos','affiliation':'Webapp','price':'12.00','currency':'BRL'}],'value':'12.00'} ); }" class="item-link item-link-ativo cbutton cbutton--effect-radomir">

<i class="fa fa-plus"></i> ADICIONAR</a>