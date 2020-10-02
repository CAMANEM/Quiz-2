package AbstractFactory;

public class ServicioDesign implements ServicioInformatico {

    @Override
    public void asignarTrabajo() {
        System.out.println("El trabajado ha sido asignado a diseñadores gráficos disponibles.");
    }

    @Override
    public void indicarPrecio() {
        System.out.println("Total a pagar: $50 000");
    }

    @Override
    public void informarSobrePago() {
        System.out.println("El precio es no negociable");
    }

}
