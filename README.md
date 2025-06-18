# 🏢 Room Booking System

Aplikacja webowa do rezerwacji sal konferencyjnych w firmie lub coworkingu. Projekt oparty na Django REST Framework (Python), PostgreSQL, React (TypeScript) i Dockerze.

---

## 🧰 Stack technologiczny

| Warstwa     | Technologia                        |
|-------------|------------------------------------|
| Backend     | Django + DRF + PostgreSQL          |
| Frontend    | React + TypeScript (📦 `/frontend`) |
| Auth        | JWT (Djoser)                       |
| DevOps      | Docker + Docker Compose            |
| Inne        | Swagger (drf-yasg), .env, Volume DB |

---

## 📦 Funkcjonalności

### 👤 Użytkownik:
- Rejestracja i logowanie (JWT)
- Przeglądanie dostępnych sal
- Rezerwacja sali na wybraną datę i godzinę
- Historia swoich rezerwacji

### 🛠️ Admin:
- Dodawanie, edytowanie i usuwanie sal
- Podgląd rezerwacji wszystkich użytkowników
- Panel admina Django (`/admin`)

---

## 🚀 Uruchomienie projektu

### Wymagania:
- Docker + Docker Compose
- (opcjonalnie) Python 3.10+ i Node.js (jeśli bez Dockera)

### 🔧 Klonowanie repo:
git clone https://github.com/your-username/room-booking.git
cd room-booking
