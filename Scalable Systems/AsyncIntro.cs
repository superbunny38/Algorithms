using System;
using System.Drawing;
using System.Net.Http;
using System.Windows.Forms;

public class AsyncIntro : Form
{
    // IMPORTANT: HttpClient is designed to be instantiated once and reused 
    // throughout the life of an application. Creating a new one for every 
    // request can exhaust your system's network sockets.
    private static readonly HttpClient client = new HttpClient();
    
    private readonly Label label;
    private readonly Button button;

    public AsyncIntro()
    {
        label = new Label
        {
            Location = new Point(10, 20),
            Text = "Length"
        };
        button = new Button
        {
            Location = new Point(10, 50),
            Text = "Click"
        };
        
        // IMPORTANT: Event Subscriptions. We are telling the button, 
        // "When someone clicks you, run the DisplayWebSiteLength method."
        button.Click += DisplayWebSiteLength; 
        
        AutoSize = true;
        Controls.Add(label);
        Controls.Add(button);
    }

    // IMPORTANT: 'async void' should ONLY be used for event handlers. 
    // Normal asynchronous methods should return 'Task' or 'Task<T>'. 
    // Returning void means the caller cannot track when this method finishes 
    // or catch exceptions it throws easily, which is fine for UI click events 
    // but bad for normal methods.
    async void DisplayWebSiteLength(object sender, EventArgs e)
    {
        label.Text = "Fetching...";
        try 
        {
            // IMPORTANT: The 'await' keyword. This is where the magic happens.
            // It tells the compiler: "Start downloading this string. While we wait, 
            // pause this method and give control BACK to the UI so the app doesn't freeze."
            string text = await client.GetStringAsync("http://csharpindepth.com"); 
            
            // IMPORTANT: UI Thread Synchronization. 
            // In Windows apps, you can only update the UI (like label.Text) from the 
            // main UI thread. The 'await' keyword is smart enough to capture the 
            // context. When the download finishes, it resumes this method exactly 
            // on the UI thread, making it safe to update the label!
            label.Text = text.Length.ToString(); 
        }
        catch (Exception ex)
        {
            label.Text = "Error: " + ex.Message;
        }
    }

    // IMPORTANT: [STAThread] is required for Windows Forms applications. 
    // It tells Windows how to handle the memory and messaging for the UI thread.
    [STAThread] 
    static void Main()
    {
        Application.EnableVisualStyles();
        Application.SetCompatibleTextRenderingDefault(false);
        Application.Run(new AsyncIntro()); 
    }
}