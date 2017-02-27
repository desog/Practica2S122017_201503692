package interfaz;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Diego
 */
import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.logging.Level;
import javax.swing.JOptionPane;
public class TestWebServer {
     public static OkHttpClient webClient = new OkHttpClient();
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
//        String nombre = "Marco";
//        RequestBody formBody = new FormEncodingBuilder()
//                .add("dato", nombre)
//
//                .build();
//        String r = getString("metodoWeb", formBody); 
//        System.out.println(r + "---");
    }
    
    public  void insertarLista(String dato){
        RequestBody Cuerpo = new FormEncodingBuilder()
                .add("dato", dato)
                .build();
        String r = getString("metodoWeb", Cuerpo);
        System.out.println(r + "!!!!");
                
    }
    
    public void eliminarLista(String dato){
        RequestBody Cuerpoe = new FormEncodingBuilder()
                .add("indice", dato)
                .build();
        String r = getString("eliminar",Cuerpoe);
        System.out.println(r+"!!");
    }
    
    public void buscarLista(String dato){
        RequestBody Cuerpob = new FormEncodingBuilder()
                .add("dato", dato)
                .build();
        String r = getString("busqueda",Cuerpob);
        System.out.println(r+"!!");
        JOptionPane.showConfirmDialog(null, "Indice de "+ dato +" "+ r);
    }
    
    //PARA COLA
    
    public void encolar(String dato){
    RequestBody Cuerpoe = new FormEncodingBuilder()
                .add("dato", dato)
                .build();
        String r = getString("encolar",Cuerpoe);
        System.out.println(r+"!!");
        JOptionPane.showConfirmDialog(null, "Indice de "+ dato +" "+ r);
    }
    
    public void desencolar(){
    RequestBody Cuerpoe = new FormEncodingBuilder()
                .add("dato", "a")
                .build();
        String r = getString("desencolar",Cuerpoe);
        System.out.println(r+"!!");
       
    }
 
     public  String getString(String metodo, RequestBody formBody) {

        try {
            URL url = new URL("http://0.0.0.0:5000/" + metodo);
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(interfaz.TestWebServer.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception ex) {
            java.util.logging.Logger.getLogger(interfaz.TestWebServer.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }

}
