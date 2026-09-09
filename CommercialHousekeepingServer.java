import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.io.*;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.util.*;

/**
 * REVATI ENTERPRISES - Commercial Housekeeping & Facility Management
 * Secure Java Backend Server & REST API Engine
 */
public class CommercialHousekeepingServer {

    private static final int PORT = 8080;
    private static final String JWT_SECRET = "RevatiEnterprises_Secure_JWT_Secret_Key_2026_HMACSHA256_Signature";

    // Client Credentials Database
    private static final Map<String, UserRecord> USER_DATABASE = new HashMap<>();

    static {
        USER_DATABASE.put("admin", new UserRecord(1, "Revati Administrator", "admin", "admin123", "ADMIN", "admin@revatienterprises.com", "+91 9876543210"));
        USER_DATABASE.put("supervisor", new UserRecord(2, "Rajesh Sharma", "supervisor", "super123", "SUPERVISOR", "rajesh.supervisor@revatienterprises.com", "+91 9812345678"));
        USER_DATABASE.put("housekeeper1", new UserRecord(3, "Suresh Kumar", "housekeeper1", "staff123", "STAFF", "suresh.k@revatienterprises.com", "+91 9712345678"));
        USER_DATABASE.put("tech1", new UserRecord(4, "Vikram Singh", "tech1", "tech123", "TECHNICIAN", "vikram.tech@revatienterprises.com", "+91 9512345678"));
        USER_DATABASE.put("manager", new UserRecord(5, "Executive Manager", "manager", "mgmt123", "MANAGEMENT", "manager@revatienterprises.com", "+91 9312345678"));
    }

    public static void main(String[] args) throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress(PORT), 0);

        // API Context Registration
        server.createContext("/api/health", new HealthHandler());
        server.createContext("/api/auth/login", new LoginHandler());
        server.createContext("/api/auth/verify", new VerifyTokenHandler());
        server.createContext("/api/employees", new EmployeesHandler());
        server.createContext("/api/attendance", new AttendanceHandler());
        server.createContext("/api/tasks", new TasksHandler());
        server.createContext("/api/complaints", new ComplaintsHandler());
        server.createContext("/api/inventory", new InventoryHandler());
        server.createContext("/api/reports", new ReportsHandler());
        server.createContext("/api/users", new UsersHandler());

        // Static File Server
        server.createContext("/", new StaticFileHandler());

        server.setExecutor(null);
        System.out.println("==========================================================================");
        System.out.println(" REVATI ENTERPRISES - FACILITY OPERATIONS BACKEND SERVER ");
        System.out.println(" JWT Security Active | CORS Options Enabled");
        System.out.println(" Running live on: http://localhost:" + PORT);
        System.out.println("==========================================================================");
        server.start();
    }

    // Cors Response Utility
    private static boolean handleCorsPreflight(HttpExchange exchange) throws IOException {
        exchange.getResponseHeaders().set("Access-Control-Allow-Origin", "*");
        exchange.getResponseHeaders().set("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS");
        exchange.getResponseHeaders().set("Access-Control-Allow-Headers", "Content-Type, Authorization, X-Requested-With");
        exchange.getResponseHeaders().set("Access-Control-Max-Age", "3600");

        if ("OPTIONS".equalsIgnoreCase(exchange.getRequestMethod())) {
            exchange.sendResponseHeaders(204, -1);
            return true;
        }
        return false;
    }

    // Health Handler
    static class HealthHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            if (handleCorsPreflight(exchange)) return;
            sendJsonResponse(exchange, 200, "{\"status\":\"UP\",\"system\":\"Revati Enterprises Facility Management Platform\",\"security\":\"JWT HMAC-SHA256\"}");
        }
    }

    // Login Handler
    static class LoginHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            if (handleCorsPreflight(exchange)) return;

            if (!"POST".equalsIgnoreCase(exchange.getRequestMethod())) {
                sendJsonResponse(exchange, 405, "{\"error\":\"Method Not Allowed\"}");
                return;
            }

            String body = readRequestBody(exchange);
            Map<String, String> params = parseJson(body);

            String username = params.getOrDefault("username", "").trim();
            String password = params.getOrDefault("password", "").trim();

            UserRecord user = USER_DATABASE.get(username.toLowerCase());
            if (user != null && user.password.equals(password)) {
                long now = System.currentTimeMillis();
                long exp = now + 86400000;

                String token = generateJwtToken(user.id, user.username, user.role, exp);
                String json = String.format("{\"success\":true,\"token\":\"%s\",\"user\":{\"id\":%d,\"name\":\"%s\",\"username\":\"%s\",\"role\":\"%s\",\"email\":\"%s\",\"phone\":\"%s\"}}",
                        token, user.id, user.name, user.username, user.role, user.email, user.phone);
                sendJsonResponse(exchange, 200, json);
            } else {
                sendJsonResponse(exchange, 401, "{\"success\":false,\"message\":\"Invalid username or password\"}");
            }
        }
    }

    // Verify Handler
    static class VerifyTokenHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            if (handleCorsPreflight(exchange)) return;

            String authHeader = exchange.getRequestHeaders().getFirst("Authorization");
            if (authHeader != null && authHeader.startsWith("Bearer ")) {
                String token = authHeader.substring(7);
                Claims claims = verifyJwtToken(token);
                if (claims != null && claims.exp > System.currentTimeMillis()) {
                    sendJsonResponse(exchange, 200, String.format("{\"valid\":true,\"user\":{\"username\":\"%s\",\"role\":\"%s\"}}", claims.username, claims.role));
                    return;
                }
            }
            sendJsonResponse(exchange, 401, "{\"valid\":false,\"message\":\"Invalid or expired token\"}");
        }
    }

    // Employees Handler
    static class EmployeesHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            if (handleCorsPreflight(exchange)) return;
            String json = "[\n" +
                    "  {\"id\":101,\"empCode\":\"REV-001\",\"name\":\"Suresh Kumar\",\"department\":\"Housekeeping\",\"designation\":\"Senior Housekeeper\",\"contact\":\"+91 9712345678\",\"joiningDate\":\"2024-01-15\",\"status\":\"Active\",\"shift\":\"Morning (07:00 - 15:30)\",\"efficiency\":98},\n" +
                    "  {\"id\":102,\"empCode\":\"REV-002\",\"name\":\"Pooja Patil\",\"department\":\"Housekeeping\",\"designation\":\"Housekeeping Attendant\",\"contact\":\"+91 9612345678\",\"joiningDate\":\"2024-03-01\",\"status\":\"Active\",\"shift\":\"Morning (07:00 - 15:30)\",\"efficiency\":94},\n" +
                    "  {\"id\":103,\"empCode\":\"REV-003\",\"name\":\"Ramesh Pawar\",\"department\":\"Housekeeping\",\"designation\":\"Deep Cleaning Specialist\",\"contact\":\"+91 9654321098\",\"joiningDate\":\"2024-05-10\",\"status\":\"Active\",\"shift\":\"Evening (15:00 - 23:30)\",\"efficiency\":91},\n" +
                    "  {\"id\":104,\"empCode\":\"REV-004\",\"name\":\"Vikram Singh\",\"department\":\"Maintenance\",\"designation\":\"Electrical Lead Engineer\",\"contact\":\"+91 9512345678\",\"joiningDate\":\"2023-11-20\",\"status\":\"Active\",\"shift\":\"General (09:00 - 17:30)\",\"efficiency\":99},\n" +
                    "  {\"id\":105,\"empCode\":\"REV-005\",\"name\":\"Amit Verma\",\"department\":\"Maintenance\",\"designation\":\"Plumbing & Elevator Specialist\",\"contact\":\"+91 9412345678\",\"joiningDate\":\"2024-02-12\",\"status\":\"Active\",\"shift\":\"General (09:00 - 17:30)\",\"efficiency\":95}\n" +
                    "]";
            sendJsonResponse(exchange, 200, json);
        }
    }

    // Attendance Handler
    static class AttendanceHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            if (handleCorsPreflight(exchange)) return;
            String json = "[\n" +
                    "  {\"id\":201,\"empCode\":\"REV-001\",\"empName\":\"Suresh Kumar\",\"date\":\"2026-08-08\",\"clockIn\":\"07:02 AM\",\"clockOut\":\"03:30 PM\",\"status\":\"Present\",\"hoursWorked\":8.5},\n" +
                    "  {\"id\":202,\"empCode\":\"REV-002\",\"empName\":\"Pooja Patil\",\"date\":\"2026-08-08\",\"clockIn\":\"07:05 AM\",\"clockOut\":\"03:28 PM\",\"status\":\"Present\",\"hoursWorked\":8.4}\n" +
                    "]";
            sendJsonResponse(exchange, 200, json);
        }
    }

    // Tasks Handler
    static class TasksHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            if (handleCorsPreflight(exchange)) return;
            String json = "[\n" +
                    "  {\"id\":301,\"taskCode\":\"REV-HK101\",\"title\":\"Executive Suite 401 Deep Cleaning\",\"area\":\"4th Floor - Suite 401\",\"assignedTo\":\"Suresh Kumar\",\"frequency\":\"Daily\",\"priority\":\"High\",\"status\":\"Completed\",\"date\":\"2026-08-08\",\"notes\":\"Sanitized washroom & eco-toiletries\",\"inspectedBy\":\"Rajesh Sharma\"},\n" +
                    "  {\"id\":302,\"taskCode\":\"REV-HK102\",\"title\":\"Glass Facade 20ft Hydrophobic Clean\",\"area\":\"Main Atrium\",\"assignedTo\":\"Pooja Patil\",\"frequency\":\"Daily\",\"priority\":\"Medium\",\"status\":\"Ongoing\",\"date\":\"2026-08-08\",\"notes\":\"Auto-scrubbing underway\",\"inspectedBy\":\"Pending\"}\n" +
                    "]";
            sendJsonResponse(exchange, 200, json);
        }
    }

    // Complaints Handler
    static class ComplaintsHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            if (handleCorsPreflight(exchange)) return;
            String json = "[\n" +
                    "  {\"id\":401,\"ticketNo\":\"REV-MNT901\",\"title\":\"AHU-2 Air Conditioning Cooling Defect\",\"category\":\"HVAC\",\"location\":\"3rd Floor Server Room\",\"reportedBy\":\"Rajesh Sharma\",\"assignedTo\":\"Vikram Singh\",\"priority\":\"Urgent\",\"status\":\"In Progress\",\"reportedDate\":\"2026-08-08 10:15 AM\",\"description\":\"Blower noise\",\"resolution\":\"Capacitor replaced\"}\n" +
                    "]";
            sendJsonResponse(exchange, 200, json);
        }
    }

    // Inventory Handler
    static class InventoryHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            if (handleCorsPreflight(exchange)) return;
            String json = "[\n" +
                    "  {\"id\":501,\"itemCode\":\"REV-INV01\",\"name\":\"Revati Hospital Grade Disinfectant (5L)\",\"category\":\"Chemicals\",\"quantity\":45,\"unit\":\"Cans\",\"reorderLevel\":15,\"unitCost\":850,\"status\":\"In Stock\",\"supplier\":\"CleanChem India\"},\n" +
                    "  {\"id\":502,\"itemCode\":\"REV-INV02\",\"name\":\"Microfiber Cleaning Cloths (Pack of 10)\",\"category\":\"Supplies\",\"quantity\":8,\"unit\":\"Packs\",\"reorderLevel\":12,\"unitCost\":350,\"status\":\"Low Stock\",\"supplier\":\"TexPro Linens\"}\n" +
                    "]";
            sendJsonResponse(exchange, 200, json);
        }
    }

    // Reports Handler
    static class ReportsHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            if (handleCorsPreflight(exchange)) return;
            String json = "[\n" +
                    "  {\"id\":601,\"title\":\"Revati Enterprises Daily Operational Summary\",\"type\":\"Daily\",\"generatedDate\":\"2026-08-08\",\"period\":\"Today\",\"completedTasks\":18,\"pendingTasks\":4,\"resolvedComplaints\":3,\"openComplaints\":2,\"attendanceRate\":\"98%\"}\n" +
                    "]";
            sendJsonResponse(exchange, 200, json);
        }
    }

    // Users Handler
    static class UsersHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            if (handleCorsPreflight(exchange)) return;
            String json = "[\n" +
                    "  {\"id\":1,\"name\":\"Revati Administrator\",\"username\":\"admin\",\"role\":\"ADMIN\",\"email\":\"admin@revatienterprises.com\",\"phone\":\"+91 9876543210\"},\n" +
                    "  {\"id\":2,\"name\":\"Rajesh Sharma\",\"username\":\"supervisor\",\"role\":\"SUPERVISOR\",\"email\":\"rajesh.supervisor@revatienterprises.com\",\"phone\":\"+91 9812345678\"},\n" +
                    "  {\"id\":3,\"name\":\"Suresh Kumar\",\"username\":\"housekeeper1\",\"role\":\"STAFF\",\"email\":\"suresh.k@revatienterprises.com\",\"phone\":\"+91 9712345678\"},\n" +
                    "  {\"id\":4,\"name\":\"Vikram Singh\",\"username\":\"tech1\",\"role\":\"TECHNICIAN\",\"email\":\"vikram.tech@revatienterprises.com\",\"phone\":\"+91 9512345678\"},\n" +
                    "  {\"id\":5,\"name\":\"Executive Manager\",\"username\":\"manager\",\"role\":\"MANAGEMENT\",\"email\":\"manager@revatienterprises.com\",\"phone\":\"+91 9312345678\"}\n" +
                    "]";
            sendJsonResponse(exchange, 200, json);
        }
    }

    // Static Web Asset Handler
    static class StaticFileHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            String path = exchange.getRequestURI().getPath();
            if (path.equals("/")) {
                path = "/index.html";
            }

            File file = new File("." + path);
            if (file.exists() && !file.isDirectory()) {
                byte[] fileBytes = Files.readAllBytes(file.toPath());
                String contentType = getContentType(path);
                exchange.getResponseHeaders().set("Content-Type", contentType);
                exchange.getResponseHeaders().set("Access-Control-Allow-Origin", "*");
                exchange.sendResponseHeaders(200, fileBytes.length);
                OutputStream os = exchange.getResponseBody();
                os.write(fileBytes);
                os.close();
            } else {
                String error = "404 Not Found";
                exchange.sendResponseHeaders(404, error.length());
                OutputStream os = exchange.getResponseBody();
                os.write(error.getBytes());
                os.close();
            }
        }

        private String getContentType(String path) {
            if (path.endsWith(".html")) return "text/html";
            if (path.endsWith(".css")) return "text/css";
            if (path.endsWith(".js")) return "application/javascript";
            if (path.endsWith(".png")) return "image/png";
            if (path.endsWith(".jpg") || path.endsWith(".jpeg")) return "image/jpeg";
            return "text/plain";
        }
    }

    // HMAC-SHA256 JWT Token Helpers
    private static String generateJwtToken(int userId, String username, String role, long exp) {
        String header = Base64.getUrlEncoder().withoutPadding().encodeToString("{\"alg\":\"HS256\",\"typ\":\"JWT\"}".getBytes(StandardCharsets.UTF_8));
        String payloadJson = String.format("{\"sub\":%d,\"username\":\"%s\",\"role\":\"%s\",\"exp\":%d}", userId, username, role, exp);
        String payload = Base64.getUrlEncoder().withoutPadding().encodeToString(payloadJson.getBytes(StandardCharsets.UTF_8));
        String signature = hmacSha256(header + "." + payload, JWT_SECRET);
        return header + "." + payload + "." + signature;
    }

    private static Claims verifyJwtToken(String token) {
        try {
            String[] parts = token.split("\\.");
            if (parts.length != 3) return null;

            String signature = hmacSha256(parts[0] + "." + parts[1], JWT_SECRET);
            if (!signature.equals(parts[2])) return null;

            String payloadJson = new String(Base64.getUrlDecoder().decode(parts[1]), StandardCharsets.UTF_8);
            Map<String, String> map = parseJson(payloadJson);

            Claims claims = new Claims();
            claims.userId = Integer.parseInt(map.getOrDefault("sub", "0"));
            claims.username = map.getOrDefault("username", "");
            claims.role = map.getOrDefault("role", "");
            claims.exp = Long.parseLong(map.getOrDefault("exp", "0"));
            return claims;
        } catch (Exception e) {
            return null;
        }
    }

    private static String hmacSha256(String data, String secret) {
        try {
            Mac mac = Mac.getInstance("HmacSHA256");
            SecretKeySpec secretKey = new SecretKeySpec(secret.getBytes(StandardCharsets.UTF_8), "HmacSHA256");
            mac.init(secretKey);
            byte[] rawHmac = mac.doFinal(data.getBytes(StandardCharsets.UTF_8));
            return Base64.getUrlEncoder().withoutPadding().encodeToString(rawHmac);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    private static void sendJsonResponse(HttpExchange exchange, int statusCode, String jsonResponse) throws IOException {
        byte[] responseBytes = jsonResponse.getBytes(StandardCharsets.UTF_8);
        exchange.getResponseHeaders().set("Access-Control-Allow-Origin", "*");
        exchange.getResponseHeaders().set("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS");
        exchange.getResponseHeaders().set("Access-Control-Allow-Headers", "Content-Type, Authorization, X-Requested-With");
        exchange.getResponseHeaders().set("Content-Type", "application/json");
        exchange.sendResponseHeaders(statusCode, responseBytes.length);
        OutputStream os = exchange.getResponseBody();
        os.write(responseBytes);
        os.close();
    }

    private static String readRequestBody(HttpExchange exchange) throws IOException {
        InputStream is = exchange.getRequestBody();
        Scanner scanner = new Scanner(is, StandardCharsets.UTF_8.name()).useDelimiter("\\A");
        return scanner.hasNext() ? scanner.next() : "";
    }

    private static Map<String, String> parseJson(String json) {
        Map<String, String> map = new HashMap<>();
        if (json == null || json.trim().isEmpty()) return map;
        json = json.trim().replaceAll("^\\{|\\}$", "");
        String[] pairs = json.split(",");
        for (String pair : pairs) {
            String[] kv = pair.split(":", 2);
            if (kv.length == 2) {
                String k = kv[0].trim().replaceAll("^\"|\"$", "");
                String v = kv[1].trim().replaceAll("^\"|\"$", "");
                map.put(k, v);
            }
        }
        return map;
    }

    static class UserRecord {
        int id;
        String name;
        String username;
        String password;
        String role;
        String email;
        String phone;

        UserRecord(int id, String name, String username, String password, String role, String email, String phone) {
            this.id = id;
            this.name = name;
            this.username = username;
            this.password = password;
            this.role = role;
            this.email = email;
            this.phone = phone;
        }
    }

    static class Claims {
        int userId;
        String username;
        String role;
        long exp;
    }
}
