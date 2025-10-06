document.addEventListener("DOMContentLoaded", function () {
  const ctx = document.getElementById("categoryChart");
  if (ctx) {
    const data = JSON.parse(ctx.dataset.chart); // pass data via data-chart attribute
    const chart = new Chart(ctx.getContext("2d"), {
      type: "doughnut",
      data: {
        labels: data.labels,
        datasets: [
          {
            data: data.values,
            backgroundColor: [
              "#FF6384",
              "#36A2EB",
              "#FFCE56",
              "#4BC0C0",
              "#9966FF",
              "#FF9F40",
            ],
          },
        ],
      },
      options: {
        responsive: true,
        plugins: {
          legend: { position: "bottom" },
        },
      },
    });
  }
});
