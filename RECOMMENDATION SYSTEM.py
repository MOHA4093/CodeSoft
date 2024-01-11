import java.util.*;

class RecommendationSystem {
    // Store user preferences
    private Map<String, Map<String, Integer>> preferences;

    // Constructor
    public RecommendationSystem() {
        preferences = new HashMap<>();
    }

    // Method to add user preferences
    public void addUserPreferences(String user, Map<String, Integer> itemPreferences) {
        preferences.put(user, itemPreferences);
    }

    // Method to get recommendations for a user
    public List<String> getRecommendations(String user) {
        Map<String, Integer> userPreferences = preferences.get(user);

        if (userPreferences == null) {
            System.out.println("User not found");
            return Collections.emptyList();
        }

        // Find similar users
        List<String> similarUsers = findSimilarUsers(user);

        // Generate recommendations based on similar users
        return generateRecommendations(user, similarUsers);
    }

    // Method to find similar users using a simple similarity metric
    private List<String> findSimilarUsers(String user) {
        List<String> similarUsers = new ArrayList<>();

        for (String otherUser : preferences.keySet()) {
            if (!otherUser.equals(user)) {
                // Simple similarity metric: number of common items
                Set<String> commonItems = new HashSet<>(preferences.get(user).keySet());
                commonItems.retainAll(preferences.get(otherUser).keySet());

                if (commonItems.size() > 0) {
                    similarUsers.add(otherUser);
                }
            }
        }

        return similarUsers;
    }

    // Method to generate recommendations based on similar users
    private List<String> generateRecommendations(String user, List<String> similarUsers) {
        Map<String, Integer> recommendations = new HashMap<>();

        for (String otherUser : similarUsers) {
            Map<String, Integer> otherUserPreferences = preferences.get(otherUser);

            for (String item : otherUserPreferences.keySet()) {
                // Consider items not present in the target user's preferences
                if (!preferences.get(user).containsKey(item)) {
                    // Weighted recommendation based on similarity
                    int similarityScore = 1;  // In this simple example, we assume equal weight for all similar users
                    int preference = otherUserPreferences.get(item);

                    recommendations.put(item, recommendations.getOrDefault(item, 0) + similarityScore * preference);
                }
            }
        }

        // Sort recommendations by score
        List<Map.Entry<String, Integer>> sortedRecommendations = new ArrayList<>(recommendations.entrySet());
        sortedRecommendations.sort((entry1, entry2) -> entry2.getValue().compareTo(entry1.getValue()));

        // Extract item names from sorted recommendations
        List<String> recommendedItems = new ArrayList<>();
        for (Map.Entry<String, Integer> entry : sortedRecommendations) {
            recommendedItems.add(entry.getKey());
        }

        return recommendedItems;
    }

    // Main method for testing
    public static void main(String[] args) {
        RecommendationSystem recommendationSystem = new RecommendationSystem();

        // Adding user preferences
        recommendationSystem.addUserPreferences("User1", Map.of("Movie1", 5, "Movie2", 4, "Movie3", 3));
        recommendationSystem.addUserPreferences("User2", Map.of("Movie1", 4, "Movie2", 5, "Movie4", 4));
        recommendationSystem.addUserPreferences("User3", Map.of("Movie2", 3, "Movie3", 4, "Movie5", 5));

        // Getting recommendations for a user
        List<String> user1Recommendations = recommendationSystem.getRecommendations("User1");

        // Displaying recommendations
        System.out.println("Recommendations for User1: " + user1Recommendations);
    }
}