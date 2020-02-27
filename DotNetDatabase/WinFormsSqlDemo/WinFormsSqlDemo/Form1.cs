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

            foreach (Orders order in cust.Orders)
            {
                MessageBox.Show($"{order.ShipAddress} {order.OrderDate}");
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            NorthwindEntities entities = new NorthwindEntities();
            List<Customers> custs = entities.Customers.ToList();

            MessageBox.Show(custs.Count.ToString());
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Customers uusi = new Customers()
            {
                CustomerID = "EFTST",
                CompanyName = "Uusi asiakas EF:n kautta",
                Country = "Finland"
            };

            NorthwindEntities entities = new NorthwindEntities();
            entities.Customers.Add(uusi);
            entities.SaveChanges();

            MessageBox.Show("Uusi asiakas lisätty.");
        }

        private void button5_Click(object sender, EventArgs e)
        {
            NorthwindEntities entities = new NorthwindEntities();
            Customers cust = entities.Customers.First();

            cust.Address = "Kotikatu 123";
            cust.City = "Oulu";

            entities.SaveChanges();

            MessageBox.Show("Asiakkaan osoitetiedosto muutettu.");
        }

        private void button6_Click(object sender, EventArgs e)
        {
            int[] luvut = { 6, 10, 5, 11, 8, 4, 2, 7, 1, 3, 9 };

            /*
            // tulosta luvut > 5 numerojärjestyksessä
            List<int> suuretLuvut = new List<int>();
            foreach (int luku in luvut)
            {
                if (luku > 5)
                {
                    suuretLuvut.Add(luku);
                }
            }
            suuretLuvut.Sort();
            foreach (int luku in suuretLuvut)
            {
                MessageBox.Show(luku.ToString());
            }
            */

            List<int> suuretLuvut = (from l in luvut
                                     where l > 5
                                     orderby l
                                     select l).ToList();
            foreach (int luku in suuretLuvut)
            {
                MessageBox.Show(luku.ToString());
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            NorthwindEntities entities = new NorthwindEntities();

            List<Customers> suomalaiset = (from c in entities.Customers
                                           where c.Country == "Finland"
                                           orderby c.CompanyName
                                           select c).ToList();

            foreach (Customers asiakas in suomalaiset)
            {
                MessageBox.Show($"{asiakas.CompanyName} {asiakas.Country}");
            }
        }
    }
}
