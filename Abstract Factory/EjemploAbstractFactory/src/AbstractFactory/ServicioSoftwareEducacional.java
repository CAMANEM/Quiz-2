package AbstractFactory;

public class ServicioSoftwareEducacional implements ServicioInformatico {

    @Override
    public void asignarTrabajo() {
        System.out.println("Nuestros programadores han sido informados del programa que deben realizar.");
    }

    @Override
    public void indicarPrecio() {

        System.out.println("Total a pagar: $30 000");
    }

    @Override
    public void informarSobrePago() {
        System.out.println("El precio es no negociable ");
    }

}
