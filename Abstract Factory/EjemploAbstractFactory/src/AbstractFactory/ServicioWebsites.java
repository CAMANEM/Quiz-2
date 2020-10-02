package AbstractFactory;

public class ServicioWebsites implements ServicioInformatico {

    @Override
    public void asignarTrabajo() {
        System.out.println("El personal encargado del desarrollo de sitios web ha aceptado el trabajo.");
    }

    @Override
    public void indicarPrecio() {
        System.out.println("Total a pagar: $20 000");
    }

    @Override
    public void informarSobrePago() {
        System.out.println("El precio es no negociable ");
    }

}
