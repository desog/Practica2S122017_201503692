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
public class web {
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
    
    
    public void desencolar(){
    RequestBody Cuerpoe = new FormEncodingBuilder()
                .add("p", "a")
                .build();
        String r = getString("tarea2",Cuerpoe);
        System.out.println(r+"!!");
       
    }
    
    
    
    
    
 
     public  String getString(String metodo, RequestBody formBody) {

        try {
            URL url = new URL("http://desog.pythonanywhere.com/" + metodo);
            Request request = new Request   .Builder().url(url).post(formBody).build();
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