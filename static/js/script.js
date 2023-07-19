import { jsPDF } from "jspdf"
function saveAsPDF() {

  const pdf = new jsPDF();
  
  // Получаем элемент с контентом, который нужно сохранить
  const content = document.getElementById('content');
  
  // Конвертируем контент в HTML
  const html = content.innerHTML;
  
  // Сохраняем HTML как PDF
  pdf.fromHTML(html, 10, 10, {}, function() {
    pdf.save('page.pdf');
  });
}