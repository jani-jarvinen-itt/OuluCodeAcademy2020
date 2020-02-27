using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinFormsSqlDemo
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // avataan tietokantayhteys
            string yhteys = "Server=localhost\\SQLEXPRESS;Database=Northwind;Trusted_Connection=True;";
            SqlConnection conn = new SqlConnection(yhteys);
            SqlCommand cmd = null;
            SqlDataReader reader = null;
            try
            {
                conn.Open();

                // luetaan käyttäjän syöttämä maa
                string maa = countryTextBox.Text;

                // muodostetaan parametroitu SQL-lause
                string sql = "SELECT CompanyName FROM Customers " +
                             "WHERE Country = @Country";
                cmd = new SqlCommand(sql, conn);
                cmd.Parameters.AddWithValue("@Country", maa);

                // luetaan tulokset
                reader = cmd.ExecuteReader();
                while (reader.Read())
                {
                    MessageBox.Show(reader[0].ToString());
                }
            }
            finally
            {
                // vapautetaan resurssit
                reader?.Close();
                cmd?.Dispose();
                conn?.Dispose();
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            NorthwindEntities entities = new NorthwindEntities();
            Customers cust = entities.Customers.First();

            MessageBox.Show($"{cust.CompanyName} {cust.City}");
        }
    }
}
