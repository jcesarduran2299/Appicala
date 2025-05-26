function formatDateMonthName(dateString) {
    let fecha = new Date(dateString);
    let opciones = {
        year: "numeric",
        month: "long",
        day: "numeric",
        hour: "numeric",
        minute: "2-digit",
        hour12: true
    };
    return fecha.toLocaleDateString("es-ES", opciones);
}